#!/usr/bin/python3
"""File that makes some changes to model_state.py that contains
 the class definition of a State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,)
    name = Column(String(128))
    cities = relationship("City", backref="state", cascade="all, delete")