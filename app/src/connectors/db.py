from sqlmodel import create_engine, Session
from app.src.config import get_db_uri

engine = create_engine(get_db_uri())

def get_session():
    with Session(engine) as session:
        yield session