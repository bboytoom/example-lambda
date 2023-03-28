import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connection():
    engine = create_engine(os.environ.get('DATABASE_URL'))
    Session = sessionmaker(engine)

    return Session()
