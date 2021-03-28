#!/usr/bin/python3
'''
Class definition of a State
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    ''' State class definition for a State object in a database connection '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)


Session = sessionmaker(engine)
session = Session()

Base.metadata.create_all(engine)
