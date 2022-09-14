#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
