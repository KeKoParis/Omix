from sqlalchemy import Column, INTEGER, VARCHAR, TEXT
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'usr'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    login = Column(VARCHAR(100))
    password = Column(TEXT)
