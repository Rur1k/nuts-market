from flask import Blueprint, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from . import db

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def statistic():
    return render_template('admin/base.html')


@admin.route('/admin/login')
def login():
    return render_template('admin/login.html')