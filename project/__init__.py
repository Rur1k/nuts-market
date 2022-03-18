import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
# import cowsay
#
# cowsay.cow('I WORK')

load_dotenv()

db = SQLAlchemy()

migrate = Migrate()

UPLOAD_FOLDER = '/static/img/app'


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nuts_admin:admin@127.0.0.1:5432/nuts_market_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


def pathSave(filename):
    return os.path.join(create_app().config['UPLOAD_FOLDER'], filename)
