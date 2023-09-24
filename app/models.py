from db import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(80), nullable=False)
    phone = Column(String(20))
    email = Column(String(120))