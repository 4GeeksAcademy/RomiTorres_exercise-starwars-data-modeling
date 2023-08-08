import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    fistname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(80), nullable=False)


    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
     __tablename__ = 'media'
     id = Column(Integer, primary_key=True)
     url =  Column(String(250),nullable=False)
     post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
     __tablename__ = 'post'
     id = Column(Integer, primary_key=True)
     usre_id = Column(Integer, ForeignKey('user.id'))
     title = Column(String(50), nullable=False) 
    
class Favorites(Base):
     __tablename__ = 'favorites'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     name = Column(String(50), nullable=False)
     url =  Column(String(250),nullable=False)

class Comment(Base):
     __tablename__ = 'comment'
     id = Column(Integer, primary_key=True)
     author_id = Column(Integer, ForeignKey('user.id'))
     post_id = Column(Integer, ForeignKey('post.id'))

class Characters(Base):
    __tablename__ = 'characters' 
    id = Column(Integer, primary_key=True)
    names = Column(String(50), nullable=False)
    url =  Column(String(250),nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Planets(Base):
     __tablename__ = 'planets'
     id = Column(Integer, primary_key=True)
     names = Column(String(50), nullable=False) 
     user_id = Column(Integer, ForeignKey('user.id'))

class Starship(Base):
     __tablename__ = 'starship'
     id = Column(Integer, primary_key=True)
     names = Column(String(50), nullable=False) 
     user_id = Column(Integer, ForeignKey('user.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
