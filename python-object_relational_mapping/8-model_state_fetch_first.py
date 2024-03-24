#!/usr/bin/python3

"""
script that prints the first State object
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        url=f"mysql+mysqldb://{user}:{password}\
        @localhost:3306/{database}?charset=utf8"
    )

    connection = engine.connect()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()
    if states:
        print(f"{states.id}: {states.name}")
    else:
        print('Nothing')
    session.close()
