from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER_NAME: str = 'verstrade_sorting_application'
    DB_PASS: str = 'verstrade_sorting_api_2022'
    DB_SERVER: str = 'localhost'
    DB_NAME: str = 'verstrade_sorting_db'


settings = Settings()
