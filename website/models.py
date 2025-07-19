#database for the users and notes

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#the ids are automatically incremented by the database

class Note(db.Model):#db model is a layer or blueprint for an object thats going to be stored in our database
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))#the max we can type is 10000 with spaces and everything
    date = db.Column(db.DateTime(timezone=True), default=func.now())#func.now will give the time defaultly
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#here user is the class user   


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)#unique identification for differentiating diff users having same name
    email = db.Column(db.String(150), unique=True)#unique email for each user   
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')#evertime we create a note on this user store it as relation 