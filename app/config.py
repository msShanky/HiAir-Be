from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER_NAME: str = 'postgres'
    DB_PASS: str = 'toor'
    DB_SERVER: str = 'localhost'
    DB_NAME: str = 'hiair_db'
    DB_PORT: int = 5433


settings = Settings()
