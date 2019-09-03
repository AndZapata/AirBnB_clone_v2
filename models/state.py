#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='delete')
    else:
        @property
        def cities(self):
            ''' nice comment '''
            list_1 = []
            objetos = models.storage.all()
            for key, val in objetos.items():
                k = key.split('.')
                if k[0] == 'City' and val.state_id == str(self.id):
                    list_1.append(val)
            return list_1
