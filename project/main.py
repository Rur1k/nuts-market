import werkzeug.exceptions
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('app/index.html')


@main.app_errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('app/404.html'), 404

