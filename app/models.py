from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin




    
class Order_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100))
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(100))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer, default=0)
    visible = db.Column(db.Boolean, default=False)
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, nullable=False, default=func.now())
    cost = db.Column(db.Float)        

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), default=3)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    birthday = db.Column(db.Date, default=func.now())
    orders = db.relationship('Order')
    
    def __repr__(self):
        return f'<User {self.email}>'
    
