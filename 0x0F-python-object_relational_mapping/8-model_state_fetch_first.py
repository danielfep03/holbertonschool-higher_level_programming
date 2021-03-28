#!/usr/bin/python3
''' Script that prints the first State object from a database '''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).first()

    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
    session.close()
