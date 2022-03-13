from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, Integer, String, DateTime
# from sqlalchemy.orm import relationship
from app.db.session import Base


class User(Base):
    __tablename__ = 'app_user'

    id = Column(Integer, primary_key=True, index=True)
    unique_id = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean)
    last_login = Column(DateTime)

    class Config:
        orm_mode = True
