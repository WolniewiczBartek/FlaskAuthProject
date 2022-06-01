from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Order, Role
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if not user:
            flash('Nieprawidłowy email', category='error')
        else:
            if not check_password_hash(user.password, password):
                flash('Nieprawidłowe hasło', category='error')
            else:
                flash('Zalogowano', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home', user=current_user))
                    
    return render_template('login.html', user=current_user)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':

        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        f_name = request.form.get('first_name')
        l_name = request.form.get('last_name')
        birthday = request.form.get('birthday')
        
        exists = User.query.filter_by(email=email).first()
        
        if exists:
            flash('Ten email już istnieje', category='error')
        elif len(email) < 3:
            flash('Nieprawidłowy email', category='error')
        elif len(f_name) < 2:
            flash('Nieprawidłowe imię', category='error')
        elif len(password1) < 5:
            flash('Zbyt krótkie hasło', category='error')
        elif password1 != password2:
            flash('Różne hasła', category='error')
        else:
            user = User(email=email, role_id=3, password=generate_password_hash(password1, method='sha256'), first_name=f_name, last_name=l_name, birthday=date(int(birthday[:4]), int(birthday[5:7]), int(birthday[8:])))
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Konto stworzone', category='success')
            return redirect(url_for('views.home', user=current_user))
            
    return render_template('register.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('cart', default=None)
    return redirect(url_for('auth.login'))