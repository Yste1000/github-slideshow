from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func #Importing func for the date entry in Note-database. func.now gives the current date and time.


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Referencing foreign key 'id' from user table 'User'. Shouldn't this be ('User.id')? For some reason it should be lowerkey when referencing a foreign key.


class User(db.Model, UserMixin): #Defining the database for the user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150)) #NB, used first_name in tutorial
    notes = db.relationship('Note') #Connecting the table 'Note' to this table.