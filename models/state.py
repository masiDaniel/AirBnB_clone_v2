#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                'City',
                cascade='all, delete, delete-orphan',
                backref='state')
    else:
        @property
        def cities(self):
            """getter for list of city instances"""
            c_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    c_list.append(city)
            return c_list
