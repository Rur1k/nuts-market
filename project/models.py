# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nuts_admin:admin@127.0.0.1:5432/nuts_market_db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from . import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(13), nullable=True)
    company = db.Column(db.String(64), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    region = db.Column(db.String(64), nullable=True)
    city = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(128), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(64), nullable=True)
    manager = db.Column(db.String(64), nullable=True)
    is_superuser = db.Column(db.Boolean, default=False)
    is_staff = db.Column(db.Boolean, default=False)