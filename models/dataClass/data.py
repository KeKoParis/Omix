from sqlalchemy import Column, INTEGER, VARCHAR, TEXT
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Data(Base):
    __tablename__ = "data"
    property_id = Column(INTEGER, primary_key=True)
    electricity = Column(INTEGER)
    data = Column(INTEGER)
