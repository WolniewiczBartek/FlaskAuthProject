from flask import Blueprint, render_template, redirect, url_for
from .models import User, Order, Role, Product, Order_Product
from flask_login import login_required, current_user


crud = Blueprint('crud', __name__)

@crud.route('/users')
@login_required
def users():
    if current_user.role_id == 1 or current_user.role_id == 2:
        return render_template('users.html', user=current_user, users=User.query.all())
    else:
        return redirect(url_for('views.home', user=current_user))
    
@crud.route('/orders')
@login_required
def orders():
    if current_user.role_id == 1 or current_user.role_id == 2:
        return render_template('orders.html', user=current_user, orders=Order.query.all())
    else:
        return redirect(url_for('views.home', user=current_user))
    
@crud.route('/products')
@login_required
def products():
    if current_user.role_id == 1 or current_user.role_id == 2:
        return render_template('products.html', user=current_user, products=Product.query.all())
    else:
        return redirect(url_for('views.home', user=current_user))