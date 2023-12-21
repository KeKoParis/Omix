from sqlalchemy import Column, INTEGER, VARCHAR, TEXT, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Notification(Base):
    __tablename__ = "notifications"
    notification = Column(TEXT)
    user_id = Column(INTEGER, ForeignKey("usr.id"))
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'notification'),
    )
