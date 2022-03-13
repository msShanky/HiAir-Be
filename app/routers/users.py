from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_token_header
from app.service.user import get_users
from app.schemas import user
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/users',
    tags=['user'],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


@router.get('/')
async def read_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.get('/me')
async def read_users():
    return [{"userName": "Fake Current User"}]
