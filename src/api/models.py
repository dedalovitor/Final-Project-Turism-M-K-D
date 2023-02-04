from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
db = SQLAlchemy()
​
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
​
    favorites = db.relationship('Favorites')
    comments = db.relationship('Comments')
​
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
            # do not serialize the password, its a security breach
        }
​
​
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
​
    regions = db.relationship('Region')
​
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
​
            # do not serialize the password, its a security breach
        }
​
​
class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    user_region = db.Column(db.Integer, db.ForeignKey('user_region.id'))
    
    comments = db.relationship('Comments', backref='region', primaryjoin="and_(Comments.content_type=='Region', Comments.content_id==Region.id)")
    hotels = db.relationship('Hotel', backref='region')
    restaurants = db.relationship('Restaurant' backref='region')
    accomodation = db.relationship('Accommodation' backref='region')
    experiences = db.relationship('Experience' backref='region')
    patrimonies = db.relationship('Patrimony' backref='region')
​
​
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo
​
            # do not serialize the password, its a security breach
        }
​
class Restoration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    type_bussiness = db.Column(db.Enum("Bar", "Restaurante", "Chiringuito"), nullable=False)
    user_restoration = db.Column(db.Integer, db.ForeignKey('Region.id'))
    comments = db.relationship('Comments', backref='restoration', primaryjoin="and_(Comments.content_type=='Restoration', Comments.content_id==Restoration.id)")
​
​
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            "type_bussiness": self.type_bussiness
            # do not serialize the password, its a security breach
        }
​
class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    type_bussiness = db.Column(db.Enum("Hotel", "Hostal", "Albergue"), nullable=False)
    user_accomodation = db.Column(db.Integer, db.ForeignKey('Region.id'))
    comments = db.relationship('Comments', backref='accommodation', primaryjoin="and_(Comments.content_type=='Accommodation', Comments.content_id==Accommodation.id)")
​
​
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            "type_bussiness": self.type_bussiness
​
            # do not serialize the password, its a security breach
        }
​
class Experiences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    user_experiences = db.Column(db.Integer, db.ForeignKey('Region.id'))
    comments = db.relationship('Comments', backref='experiences', primaryjoin="and_(Comments.content_type=='Experiences', Comments.content_id==Experiences.id)")
​
​
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            
            # do not serialize the password, its a security breach
            }
​
class Patrimony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    user_patrimony = db.Column(db.Integer, db.ForeignKey('Region.id'))
    comments = db.relationship('Comments', backref='patrimony', primaryjoin="and_(Comments.content_type=='Patrimony', Comments.content_id==Patrimony.id)")
​
​
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            
            # do not serialize the password, its a security breach
            }
​
class Favorites(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'))    
    region = db.Column(db.Integer, db.ForeignKey('region.id'))
    restoration = db.Column(db.Integer, db.ForeignKey('restoration.id'))
    accommodation = db.Column(db.Integer, db.ForeignKey('accommodation.id'))
    patrimony = db.Column(db.Integer, db.ForeignKey('patrimony.id'))
​
class Comments(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.Text, nullable=False)
    user_region_id = db.Column(db.Integer, db.ForeignKey('user_region.id'))    
    region = db.Column(db.Integer, db.ForeignKey('region.id'))
    restoration = db.Column(db.Integer, db.ForeignKey('restoration.id'))
    accommodation = db.Column(db.Integer, db.ForeignKey('accommodation.id'))
    patrimony = db.Column(db.Integer, db.ForeignKey('patrimony.id'))
