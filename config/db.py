import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///local.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    """yeilds an instance of the db and closes it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
