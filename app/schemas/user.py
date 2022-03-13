from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    unique_id: str
    email: str
    full_name: str
    is_active: bool
    last_login: datetime
