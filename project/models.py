from flask_login import UserMixin
from sqlalchemy_utils import ChoiceType

from . import db

# Product models
class Product(db.Model):
    __tablename__ = 'products'
    STATUS = [
        ('Новое', 'Новое'),
        ('В наличии', 'В наличии')
    ]

    CATEGORY = [
        ('Другое', 'Другое'),
        ('Грецкий орех', 'Грецкий орех'),
        ('Фундук', 'Фундук'),
        ('Кешью', 'Кешью'),
        ('Арахис', 'Арахис'),
        ('Миндаль', 'Миндаль')
    ]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vendor_code = db.Column(db.String(255), nullable=True)
    category = db.Column(ChoiceType(CATEGORY, impl=db.String()))
    composition = db.Column(db.String(255), nullable=True)
    net_weight = db.Column(db.Integer, nullable=True)
    energy_value = db.Column(db.Integer, nullable=True)
    expiration_date = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, default=0.0)
    description = db.Column(db.String(255), nullable=True)
    main_picture = db.Column(db.String(255), nullable=True)
    count = db.Column(db.Integer, default=0)
    status = db.Column(ChoiceType(STATUS, impl=db.String()))


# User models

class User(UserMixin, db.Model):
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
    avatar = db.Column(db.String(), nullable=True)
