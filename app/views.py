from flask import Blueprint, render_template, session
from .models import User, Order, Role, Product
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html', user=current_user, products=Product.query.filter_by(visible=True).all())

@views.route('/product/<id>')
def product(id):
    return render_template('product.html', user=current_user, product=Product.query.filter_by(id=id).first())

@views.route('/add_to_cart/<prod_id>', methods=['POST'])
def add_to_cart(prod_id):
    
    if 'cart' not in session:
        session['cart'] = {}
    if str(prod_id) in session.get('cart').keys():
        session['cart'][str(prod_id)] += 1
    else:
        session['cart'][str(prod_id)] = 1
    return render_template('home.html', user=current_user)
        
@views.route('/cart')
def cart():
    if 'cart' in session:
        cart = session['cart']
    else:
        cart = None
    return render_template('cart.html', user=current_user, cart=cart)
        
        