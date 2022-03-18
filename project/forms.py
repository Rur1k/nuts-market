from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email


class AdminLoginForm(FlaskForm):
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