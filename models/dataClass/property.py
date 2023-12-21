from sqlalchemy import Column, INTEGER, VARCHAR, TEXT, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Property(Base):
    __tablename__ = "property"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    address = Column(VARCHAR(100))
    name = Column(TEXT)
    usr_id = Column(INTEGER, ForeignKey("usr.id"))
