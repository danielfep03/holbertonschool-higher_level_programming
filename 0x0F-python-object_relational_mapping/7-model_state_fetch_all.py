#!/usr/bin/python3
''' Script that lists all State objects from the database hbtn_0e_6_usa '''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(argv[1], 
                       argv[2], argv[3]))
Session = sessionmaker(engine)
session = Session()
states = session.query(State).order_by(State.id)

for state in states:
    print("{}: {}".format(state.id, state.name))
session.close()
if __name__ == '__main__':
    exit
