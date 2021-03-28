#!/usr/bin/python3
"""file that contains the class definition of a State and an instance
    Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class City(Base):
    """Defines class City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,)
    name = Column(String(128))
    state.id = Column(Integer, ForeignKey('states.id'))
