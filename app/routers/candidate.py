from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_token_header
from app.service.candidate import get_all_candidates
from app.service.user import get_users
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/candidate',
    tags=['candidate'],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)


@router.get('/')
async def read_users(db: Session = Depends(get_db)):
    return get_all_candidates(db)
