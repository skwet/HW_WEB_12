from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://postgres:fastapi123@localhost:5432/postgres'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
