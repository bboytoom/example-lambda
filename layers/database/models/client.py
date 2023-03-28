from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from config.connection_db import connection

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clientes'

    id = Column(Integer(), primary_key=True)
    name = Column(String(40), nullable=True)
    last_name = Column(String(100), nullable=True)
    address = Column(String(80), nullable=True)
    email = Column(String(70), nullable=True)

    def __str__(self):
        return self.name

    def get_all_clientes():
        return connection().query(Client).all()
