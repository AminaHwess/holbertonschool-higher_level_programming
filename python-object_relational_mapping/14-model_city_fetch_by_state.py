#!/usr/bin/python3

"""
prints all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    statecity = session.query(State, City).join(City).order_by(City.id)
    for state, city in statecity:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
