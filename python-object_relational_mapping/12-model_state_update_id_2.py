#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
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

    # ID-si 2 olan ştatı tapırıq
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Əgər tapılıbsa adını dəyişib commit edirik
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
        
    session.close()
