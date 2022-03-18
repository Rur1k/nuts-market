from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from .models import User
from .forms import AdminLoginForm
from . import db

admin = Blueprint('admin', __name__)


@admin.route('/admin')
@login_required
def statistic():
    return render_template('admin/base.html')


@admin.route('/admin/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = AdminLoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = True if form.remember.data else False

            user = User.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password) or not user.is_staff:
                flash('Данные авторизации не корректны')
                return render_template('admin/login.html', form=form)

            login_user(user, remember=remember)
            return redirect(url_for('admin.statistic'))
        else:
            pass
    else:
        form = AdminLoginForm()
    return render_template('admin/login.html', form=form)


@admin.route('/admin/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))