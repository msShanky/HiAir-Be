from fastapi import APIRouter
router = APIRouter()


@router.get('/auth/login', tags=['auth'])
async def login_user():
    return {"message": "User logged in successfully!"}


@router.get('/auth/forgot-password', tags=['auth'])
async def forgot_password():
    return {"message": "User password has been reset successfully!"}
