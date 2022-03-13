from fastapi import APIRouter, Depends

from app.dependencies import get_token_header

router = APIRouter(
    prefix='/users',
    tags=['user'],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


@router.get('/')
async def read_users():
    return [{"userName": "Rick"}, {"userName": "Morty"}]


@router.get('/me')
async def read_users():
    return [{"userName": "Fake Current User"}]
