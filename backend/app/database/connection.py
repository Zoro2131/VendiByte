#imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# imports main app settings
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)