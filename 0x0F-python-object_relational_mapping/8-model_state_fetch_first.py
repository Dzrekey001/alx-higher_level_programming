#!/usr/bin/python3
"""
    A script that prints the first State
    object from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    """
        Access to the database and get a state
        from the database.
    """
    engine = create_engine(
            "mysql://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    app_session = Session()

    first_instance = app_session.query(State).order_by(State.id).first()
    print(f"{first_instance.id}: {first_instance.name}")
