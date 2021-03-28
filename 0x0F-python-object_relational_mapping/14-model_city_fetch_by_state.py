#!/usr/bin/python3
'''Prints all City objects from the database hbtn_0e_14_usa '''

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State, City).join(City, State.id == City.state_id).\
        order_by(City.id)

    for state in states:
        print("{}: ({}) {}".format(state.State.name,
                                   state.City.id, state.City.name))
    session.close()
