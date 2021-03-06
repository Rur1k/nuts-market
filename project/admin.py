from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from .models import User, Product, Order
from .forms import AdminLoginForm, ProductForm, OrderForm
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


# order views

@admin.route('/admin/order')
@login_required
def order():
    data = {
        'orders': Order.query.all()
    }
    return render_template('admin/order/index.html', data=data)


@admin.route('/admin/order/create', methods=['POST', 'GET'])
@login_required
def order_create():
    if request.method == 'POST':
        form = OrderForm(request.form)
        form.user.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=False)]
        form.manager.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=True)]
        print(request.form)
        if form.validate():
            new_obj = Order(
                date=form.date.data,
                user_id=form.user.data,
                full_name=form.full_name.data,
                email=form.email.data,
                phone=form.phone.data,
                buy=form.buy.data,
                delivery=form.delivery.data,
                city=form.city.data,
                department=form.department.data,
                status=form.status.data,
                manager_id=form.manager.data,
                description=form.description.data,
            )

            db.session.add(new_obj)
            db.session.commit()

            flash('Заказ успешно создан!')
            return redirect(url_for('admin.order'))
        else:
            flash('Упс, а валидация то не пройдена!')
    else:
        form = OrderForm()
        form.user.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=False)]
        form.manager.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=True)]
    return render_template('admin/order/create.html', form=form)


@admin.route('/admin/order/<int:id>', methods=['GET'])
@login_required
def order_info(id):
    data = {
        'order': Order.query.filter_by(number=id).first_or_404()
    }
    return render_template('admin/order/info.html', data=data)


@admin.route('/admin/order/<int:id>/update', methods=['POST', 'GET'])
@login_required
def order_update(id):
    obj= Order.query.filter_by(number=id).first_or_404()

    if request.method == 'POST':
        form = OrderForm(request.form)
        form.user.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=False)]
        form.manager.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=True)]
        if form.validate():
            obj.date = form.date.data,
            obj.user_id = form.user.data,
            obj.full_name = form.full_name.data,
            obj.email = form.email.data,
            obj.phone = form.phone.data,
            obj.buy = form.buy.data,
            obj.delivery = form.delivery.data,
            obj.city = form.city.data,
            obj.department = form.department.data,
            obj.status = form.status.data,
            obj.manager_id = form.manager.data,
            obj.description = form.description.data,

            db.session.commit()

            flash('Заказ успешно обновлен!')
            return redirect(url_for('admin.order', id=obj.number))
        else:
            flash('Упс, а валидация то не пройдена!')
    else:
        form = OrderForm(obj=obj)
        form.user.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=False)]
        form.manager.choices = [((obj.id, obj.full_name)) for obj in User.query.filter_by(is_staff=True)]
    return render_template('admin/order/update.html', form=form, id=obj.number)


@admin.route('/admin/order/<int:id>/delete')
@login_required
def order_delete(id):
    obj = Order.query.get_or_404(id)

    try:
        db.session.delete(obj)
        db.session.commit()
        flash('Удаление прошло успешно!')
    except:
        flash('Упс, что-то пошло не так!')
    return redirect(url_for('admin.order'))
