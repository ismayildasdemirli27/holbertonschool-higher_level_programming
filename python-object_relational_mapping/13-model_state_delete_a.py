#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Verilənlər bazasına qoşuluruq
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adında 'a' hərfi olan bütün ştatları tapırıq
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Hər birini silirik və commit edirik
    for state in states_to_delete:
        session.delete(state)
        
    session.commit()
    session.close()
