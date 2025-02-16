import datetime

from sqlalchemy import Column, DateTime

from src.database.configs import Base


class BaseModel(Base):
    __abstract__ = True

    updated_at = Column(DateTime(), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = Column(DateTime(), default=datetime.datetime.utcnow)
