from sqlalchemy import create_engine, MetaData
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

metadata = MetaData()

engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)
