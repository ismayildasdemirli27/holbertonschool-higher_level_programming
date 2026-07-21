#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
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

    # Yalnız İLK obyekti çəkirik (.first() istifadə edərək)
    first_state = session.query(State).order_by(State.id).first()

    # Əgər tapıldırsa çap edirik, cədvəl boşdursa "Nothing" yazdırırıq
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
        
    session.close()
