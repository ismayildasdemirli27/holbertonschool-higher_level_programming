#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # Yeni State obyekti yaradırıq
    new_state = State(name="Louisiana")
    
    # Sessiyaya əlavə edib dəyişikliyi bazaya yazırıq (commit)
    session.add(new_state)
    session.commit()

    # Yeni yaradılan ştatın ID-sini ekrana çap edirik
    print(new_state.id)
        
    session.close()
