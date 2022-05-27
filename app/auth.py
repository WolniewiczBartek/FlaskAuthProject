from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.data
    else:
        return render_template("login.html")

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':

        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        birthday = request.form.get('birthday')

        if len(email) < 3:
            flash('Nieprawidłowy email', category='error')
        elif len(first_name) < 2:
            flash('Nieprawidłowe imię', category='error')
        elif len(password1) < 5:
            flash('Zbyt krótkie hasło', category='error')
        elif password1 != password2:
            flash('Różne hasła', category='error')
        else:
            flash('Konto stworzone', category='succsess')
        
    
    return render_template("register.html")

@auth.route('/logout')
def logout():
    return "logout"