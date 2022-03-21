import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings


postgres = 'postgresql'
mysql = 'mysql'

SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(
    postgres,
    settings.DB_USER_NAME,
    settings.DB_PASS,
    settings.DB_SERVER,
    settings.DB_PORT,
    settings.DB_NAME
)

print("THE SQL DATABASE CONNECTION URL IS", os.getenv('DATABASE_URL'))
print("THE SQL DATABASE CONNECTION URL FORMED IS", SQLALCHEMY_DATABASE_URL)
engine = create_engine(os.getenv('DATABASE_URL', SQLALCHEMY_DATABASE_URL), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
