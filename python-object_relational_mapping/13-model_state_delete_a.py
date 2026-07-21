#!/usr/bin/python3
"""
List all State objects from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    usnm = argv[1]
    pwd = argv[2]
    db = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{usnm}:{pwd}@localhost:3306/{db}",
        future=True
    )

    Session = sessionmaker(bind=engine, future=True)
    session = Session()

    state = session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session=False
    )

    session.commit()
    session.close()
