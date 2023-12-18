from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Profile(Base):
    __tablename__ = "profile"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    phone_num = Column(INTEGER)
    email = Column(VARCHAR(100))
    usr_id = Column(INTEGER)
