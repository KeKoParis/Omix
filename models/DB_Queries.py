from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app_config import engine
from models.CRUD import CRUD
from models.dataClass.data import Data
from models.dataClass.notifications import Notification
from models.dataClass.property import Property
from models.dataClass.user import User
from models.dataClass.profile import Profile

class Queries:

    def __init__(self):
        self.crud = CRUD()
        self.session = sessionmaker(bind=engine)

    def get_property_by_user(self, login: str):
        """

        :param login:
        :return: [User, Property]
        """
        curr_user = self.crud.read(User, login=login)[0]

        with self.session(bind=engine, expire_on_commit=True) as db:
            try:
                result = db.query(User, Property).join(Property, Property.usr_id == User.id).filter(
                    User.id == curr_user.id).all()
                return result
            except SQLAlchemyError as err:
                print(err)
                return None

    def get_property_indicators(self, prop):
        """

        :param prop:
        :return: [Property ,Data]
        """
        print("prop ", prop)
        curr_prop = self.crud.read(Property, id=prop.id)[0]

        with self.session(bind=engine, expire_on_commit=True) as db:
            try:
                result = db.query(Property, Data).join(Data, Data.property_id == Property.id).filter(
                    Property.id == curr_prop.id).all()
                return result
            except SQLAlchemyError as err:
                print(err)
                return None

    def get_notifications_by_user(self, login):
        """

        :param login:
        :return: [User, Notification]
        """
        curr_user = self.crud.read(User, login=login)[0]
        print("notifiactionsnameuser  ", curr_user.login)
        with self.session(bind=engine, expire_on_commit=True) as db:
            try:
                result = db.query(User, Notification).join(Notification, Notification.user_id == User.id).filter(
                    User.id == curr_user.id).all()
                print("result notif ", result[0])
                return result
            except SQLAlchemyError as err:
                print(err)
                return None

    def get_user_profile(self, login):
        curr_user = self.crud.read(User, login=login)[0]
        with self.session(bind=engine, expire_on_commit=True) as db:
            try:
                result = db.query(User, Profile).join(Profile, Profile.usr_id == User.id).filter(
                    User.id == curr_user.id).all()

                return result
            except SQLAlchemyError as err:
                print(err)
                return None

    def get_stats_for_period(self):
        pass
# a = Queries()
#
# print(len(a.get_property_by_user('stas')))
# for i in a.get_property_by_user('stas'):
#     print(i[1])
