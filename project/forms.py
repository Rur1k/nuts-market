from flask_wtf import FlaskForm
from wtforms.fields  import SelectField, TextAreaField, EmailField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email
from wtforms_alchemy import ModelForm, ModelFieldList

from .models import Product, Order, User


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

    description = TextAreaField()


class OrderForm(ModelForm):
    class Meta:
        model = Order

    user = SelectField(coerce=int)
    manager = SelectField(coerce=int)
    description = TextAreaField()

