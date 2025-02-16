from sqlalchemy import Column, Integer, String, DateTime, Boolean

from src.database.configs import Base
from src.shared_model import BaseModel


class UserModel(BaseModel, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    full_name = Column(String, nullable=False)
    username = Column(String, nullable=True, default=None)
    password = Column(String, nullable=False)
    bio = Column(String, nullable=True)
    image = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    last_seen = Column(DateTime)
    online_status = Column(Boolean, default=False, nullable=False)
