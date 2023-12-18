from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from app_config import engine
from models.dataClass.user import User


def log_in(login: str):
    session = sessionmaker(autoflush=False, bind=engine)

    with session(bind=engine, expire_on_commit=True) as db:
        try:
            user = db.query(User).filter(User.login == login).first()
            return user
        except SQLAlchemyError as err:
            print(err)
            return False


def register(login: str, password: str):
    user = User()
    user.login = login
    user.password = password
    session = sessionmaker(autoflush=False, bind=engine)

    with session(bind=engine, expire_on_commit=True) as db:
        try:
            db.add(user)
            db.commit()
            return True
        except SQLAlchemyError as err:
            print(err)
            return False
