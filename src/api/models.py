from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    favorites = db.relationship('Favorite')
    comments = db.relationship('Comment')

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
            # do not serialize the password, its a security breach
        }


class User_region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    contact_person_name = db.Column(db.String(100), unique=True, nullable=False)
    nif = db.Column(db.String(100), unique=True, nullable=False)
    contact_person_telf = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    country= db.Column(db.String(100), unique=True, nullable=False)
    city = db.Column(db.String(100), unique=True, nullable=False)

    regions = db.relationship('Region')


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "contact_person_name": self.contact_person_name,
            "nif": self.nif,
            "contact_person_telf": self.contact_person_telf,
            "address": self.address,
            "country": self.country,
            "city": self.city

            # do not serialize the password, its a security breach
        }


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.String(255), unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    user_region = db.Column(db.Integer, db.ForeignKey('user_region.id'))
    


    restaurants = db.relationship('Restaurant')
    hostels = db.relationship('hostel')
    experiences = db.relationship('experience')
    patrimonies = db.relationship('patrimony')


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo

            # do not serialize the password, its a security breach
        }

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.String(255), unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    user_region = db.Column(db.Integer, db.ForeignKey('user_region.id'))
    


    restaurants = db.relationship('Restaurant')
    hostels = db.relationship('hostel')
    experiences = db.relationship('experience')
    patrimonies = db.relationship('patrimony')


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo

            # do not serialize the password, its a security breach
        }