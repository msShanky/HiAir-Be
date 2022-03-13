from fastapi import Header, HTTPException
from typing import Generator
from app.db.session import SessionLocal


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
