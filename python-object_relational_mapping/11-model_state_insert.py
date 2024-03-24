#!/usr/bin/python3

"""
script that adds the State object “Louisiana” to the database
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
    New = State(name='Louisiana')
    session.add(New)
    session.commit()
    print(New.id)
    session.close()
