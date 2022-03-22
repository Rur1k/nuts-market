from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from .models import User, Product
from .forms import AdminLoginForm, ProductForm
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


# product views

@admin.route('/admin/product')
@login_required
def product():
    data = {
        'product_list': Product.query.all()
    }
    return render_template('admin/product/index.html', data=data)


@admin.route('/admin/product/create', methods=['POST', 'GET'])
@login_required
def product_create():
    if request.method == 'POST':
        form = ProductForm(request.form)
        if form.validate():
            new_product = Product(
                name=form.name.data,
                vendor_code=form.vendor_code.data,
                category=form.category.data,
                composition=form.composition.data,
                net_weight=form.net_weight.data,
                energy_value=form.energy_value.data,
                expiration_date=form.expiration_date.data,
                price=form.price.data,
                description=form.description.data,
                status=form.status.data,
            )

            db.session.add(new_product)
            db.session.commit()

            flash('Товар успешно добавлен!')
            return redirect(url_for('admin.product'))
        else:
            flash('Упс, а валидация то не пройдена!')
    else:
        form = ProductForm()
    return render_template('admin/product/create.html', form=form)


@admin.route('/admin/product/<int:id>', methods=['GET'])
@login_required
def product_info(id):
    data = {
        'product': Product.query.filter_by(id=id).first_or_404()
    }
    return render_template('admin/product/info.html', data=data)


@admin.route('/admin/product/<int:id>/update', methods=['POST', 'GET'])
@login_required
def product_update(id):
    product_information = Product.query.filter_by(id=id).first_or_404()

    if request.method == 'POST':
        form = ProductForm(request.form)
        if form.validate():
            product_information.name=form.name.data
            product_information.vendor_code=form.vendor_code.data
            product_information.category=form.category.data
            product_information.composition=form.composition.data
            product_information.net_weight=form.net_weight.data
            product_information.energy_value=form.energy_value.data
            product_information.expiration_date=form.expiration_date.data
            product_information.price=form.price.data
            product_information.description=form.description.data
            product_information.status=form.status.data

            db.session.commit()

            flash('Товар успешно обновлен!')
            return redirect(url_for('admin.product_info', id=product_information.id))
        else:
            flash('Упс, а валидация то не пройдена!')
    else:
        form = ProductForm(obj=product_information)
    return render_template('admin/product/update.html', form=form, id=product_information.id)


@admin.route('/admin/product/<int:id>/delete')
@login_required
def product_delete(id):
    obj = Product.query.get_or_404(id)

    try:
        db.session.delete(obj)
        db.session.commit()
        flash('Удаление прошло успешно!')
    except:
        flash('Упс, что-то пошло не так!')
    return redirect(url_for('admin.product'))


@admin.route('/admin/product/<int:id>/edit_count', methods=['POST', 'GET'])
@login_required
def product_edit_count(id):
    product_information = Product.query.filter_by(id=id).first_or_404()

    if request.method == 'POST':
        form = request.form
        print(form.get('edit_option'))

        if form.get('edit_option') == "add":
            product_information.count = product_information.count + int(form.get('count_product'))
            db.session.commit()
            flash('Склад успешно обновлен!')
            return redirect(url_for('admin.product_info', id=product_information.id))
        elif form.get('edit_option') == "take":
            count = product_information.count - int(form.get('count_product'))
            if count < 0:
                flash('Состояние склада не может быть отрицательным!')
                return redirect(url_for('admin.product_edit_count', id=product_information.id))
            else:
                product_information.count = count
                db.session.commit()
                flash('Склад успешно обновлен!')
                return redirect(url_for('admin.product_info', id=product_information.id))
    else:
        form = ProductForm(obj=product_information)
    form = ProductForm(obj=product_information)
    return render_template('admin/product/edit_count.html', form=form, id=product_information.id)