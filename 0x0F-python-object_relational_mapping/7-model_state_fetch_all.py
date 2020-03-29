#!/usr/bin/python3
"""script that prints the first State object
 from the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                                        argv[1],
                                                                        argv[2],
                                                                        argv[3]))

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    ses = session()
    states = ses.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    ses.close()
