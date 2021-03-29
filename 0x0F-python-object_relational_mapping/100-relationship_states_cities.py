#!/usr/bin/python3
"""creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newstate = State(name="California")
    newcity = City(name="San Francisco")
    newstate.cities.append(newcity)
    session.add(newstate)
    session.commit()
    session.close()
