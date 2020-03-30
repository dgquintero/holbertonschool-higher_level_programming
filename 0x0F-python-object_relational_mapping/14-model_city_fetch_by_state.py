#!/usr/bin/python3
""" script that changes the name of a State object
from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1],
                                argv[2],
                                argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(eng)
    session = sessionmaker(bind=eng)
    ses = session()
    for state, city in ses.query(State, City)\
                          .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    ses.close()
