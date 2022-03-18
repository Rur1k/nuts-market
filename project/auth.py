import os

from flask import Blueprint, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from .models import User
from . import db, pathSave

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('app/enter.html')


@auth.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_repeat = request.form.get('password_repeat')

        user = User.query.filter_by(email=email).first()

        if user:
            return redirect(url_for('auth.registration'))
        else:
            file = request.files['file']
            if file:
                filename = secure_filename(file.filename)
                file.save(pathSave(filename))
            else:
                filename = None

            new_user = User(
                full_name=full_name,
                email=email,
                password=generate_password_hash(password, method='sha256'),
                avatar=filename
            )

            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    else:
        return render_template('app/reg-fiz.html')


@auth.route('/logout')
def logout():
    return "Logout"
