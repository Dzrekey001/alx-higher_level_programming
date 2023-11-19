#!/usr/bin/python3
"""
    A script that prints the State object with the
    name passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    app_session = Session()

    states = app_session.query(State).filter(State.name == argv[4])

    if states is not None:
        for state in states:
            print(state.id)
    else:
        print("Not found")
