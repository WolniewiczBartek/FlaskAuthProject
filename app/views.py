from flask import Blueprint, render_template
from .models import User, Order
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/users')
@login_required
def users():
    return render_template('users.html', user=current_user, users=User.query.all())