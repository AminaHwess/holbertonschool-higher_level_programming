#!/usr/bin/python3

"""
script that changes the name of a State object
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
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
