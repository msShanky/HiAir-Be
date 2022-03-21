import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USER_NAME: str = os.getenv('DB_USER_NAME','postgres')  
    DB_PASS: str = os.getenv('DB_PASS','toor')
    DB_SERVER: str = os.getenv('DB_SERVER','localhost')
    DB_NAME: str = os.getenv('DB_NAME','hiair_db') 
    DB_PORT: int = os.getenv('DB_PORT',5433) 


settings = Settings()
