import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    _tablename_ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(30), nullable=False)

class Planet(Base):
    _tablename_ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(100), nullable=False)

class Character(Base):
    _tablename_ = 'characters'
    id = Column(Integer, primary_key=True)
    char_name = Column(String(100), nullable=False)
    side = Column(Boolean, nullable=True)

class Favorite(Base):
    _tablename_ = 'favorites'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    fav_planet = Column(Integer, ForeignKey('planets.id'))
    fav_char = Column(Integer, ForeignKey('characters.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')