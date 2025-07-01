#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

# Run only executed
if __name__ == "__main__":

    # Engine creation with mysql and mysqldb DBAPI
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Creating all classes in DB
    Base.metadata.create_all(engine)

    # Creating Session and its instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Printing the result
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Closing the session
    session.close()
