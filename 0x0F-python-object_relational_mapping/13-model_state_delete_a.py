#!/usr/bin/python3
'''
Script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        session.delete(state)
    session.commit()
    session.close()
