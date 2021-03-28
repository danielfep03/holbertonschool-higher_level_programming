#!/usr/bin/python3
'''
Script that changes the name of a State object from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker()(bind=engine)
    no_state = Session.query(State).filter_by(id=2).first()
    no_state.name = 'New Mexico'
    Session.commit()

    Session.close()
