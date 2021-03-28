#!/usr/bin/python3
"""Prints the State object with the name passed
 as argument from hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = session.query(State).filter_by(id=2).first()
    i.name = 'New Mexico'
    session.commit()
    session.close()
