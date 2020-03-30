#!/usr/bin/python3
"""script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1],
                                argv[2],
                                argv[3]),
                                pool_pre_ping=True)

    Base.metadata.create_all(eng)
    session = sessionmaker(bind=eng)
    ses = session()
    states = ses.query(State).filter(State.name.like(argv[4]))\
                             .order_by(State.id).all()
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
    ses.close()
