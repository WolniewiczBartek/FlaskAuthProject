from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    birthday = db.Column(db.Date, default=func.now())
    orders = db.relationship('Order')
    
    def __repr__(self):
        return f'<User {self.email}>'