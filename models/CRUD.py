from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app_config import engine


class CRUD:
    @staticmethod
    def create(some_class, **kwargs):
        session = sessionmaker(autoflush=False, bind=engine)

        instance = some_class(**kwargs)
        with session(bind=engine, expire_on_commit=True) as db:
            try:
                db.add(instance)
                db.commit()
            except SQLAlchemyError as err:
                print(err)

    @staticmethod
    def read(some_class, **kwargs):
        session = sessionmaker(autoflush=False, bind=engine)

        with session(bind=engine, expire_on_commit=True) as db:
            try:
                result = db.query(some_class).filter_by(**kwargs).all()
                return result
            except SQLAlchemyError as err:
                print(err)

    @staticmethod
    def update_object(some_class, id, **kwargs):
        session = sessionmaker(autoflush=False, bind=engine)

        with session(bind=engine, expire_on_commit=True) as db:
            try:
                instance = db.query(some_class).get(id)
                if instance:
                    for key, value in kwargs.items():
                        setattr(instance, key, value)
                    db.commit()
                    return instance
            except SQLAlchemyError as err:
                print(err)
                return None

    @staticmethod
    def delete(instance):
        session = sessionmaker(autoflush=False, bind=engine)

        with session(bind=engine, expire_on_commit=True) as db:
            try:
                db.delete(instance)
                db.commit()
            except SQLAlchemyError as err:
                print(err)
