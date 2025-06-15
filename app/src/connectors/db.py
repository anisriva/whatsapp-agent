from sqlmodel import create_engine, Session, SQLModel
from app.src.config.db import get_db_uri

engine = create_engine(get_db_uri())

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session