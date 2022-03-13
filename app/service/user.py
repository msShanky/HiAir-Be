from statistics import mode
from sqlalchemy.orm import Session
from app.models import user as UserModel
# from app.schemas import user as UserSchema


def get_users(db: Session):
    return db.query(UserModel.User).all()
