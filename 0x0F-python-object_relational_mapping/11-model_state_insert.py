#!/usr/bin/python3
"""script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
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
    ses.add(State(name="Louisiana"))
    ses.commit()
    states = ses.query(State).filter_by(name="Louisiana").first()
    print("{}".format(states.id))
    ses.close()
