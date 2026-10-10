#imports
from collections.abc import Generator
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import SessionLocal


# dependencies

def getDb() ->Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db

    except SQLAlchemyError:
        db.rollback()
        raise

    finally:
        db.close()