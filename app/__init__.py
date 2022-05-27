from venv import create
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_db(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('Created db!')

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'fddffsdf 31duh3#@Dfasgcsh'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
        
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Order, User
    
    create_db(app)

    return app

app = create_app()
