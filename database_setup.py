import os

import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        #returns object data in easily serializeable format
        return {
            'name' : self.name,
            'id' : self.id,
            'email': self.email,
            'picture': self.picture,

        }


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        # returns object data in easily serializeable format
        return {
            'name': self.name,
            'id': self.id,
            'user_id': self.user_id,

        }

class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    category = relationship(Category)
    user = relationship(User)

    @property
    def serialize(self):
        #returns object data in easily serializeable format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'category_id' : self.category_id
        }

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
