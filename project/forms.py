from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, EmailField, BooleanField, PasswordField, FileField
from wtforms.validators import DataRequired, Email
from wtforms_alchemy import ModelForm

from .models import Product


class AdminLoginForm(FlaskForm):
    """ Форма для авторизации персонала  """
    email = EmailField(validators=[DataRequired(), Email()],
                       render_kw={
                           'class': 'form-control',
                           'placeholder': 'Email'
                       })
    password = PasswordField(validators=[DataRequired()],
                             render_kw={
                                 'class': 'form-control',
                                 'placeholder': 'Пароль'
                             })
    remember = BooleanField()


class ProductForm(ModelForm):
    class Meta:
        model = Product

    name = StringField(render_kw={'class': 'form-control'})
    vendor_code = StringField(render_kw={'class': 'form-control'})
    category = SelectField(render_kw={'class': 'form-control'})
    composition = StringField(render_kw={'class': 'form-control'})
    net_weight = StringField(render_kw={'class': 'form-control'})
    energy_value = StringField(render_kw={'class': 'form-control'})
    expiration_date = StringField(render_kw={'class': 'form-control'})
    price = StringField(render_kw={'class': 'form-control'})
    description = TextAreaField(render_kw={'class': 'form-control'})
    main_picture = FileField(render_kw={'class': 'form-control'})
    status = SelectField(render_kw={'class': 'form-control'})

