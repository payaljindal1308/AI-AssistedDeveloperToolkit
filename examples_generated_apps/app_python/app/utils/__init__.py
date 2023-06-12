
# app/utils/__init__.py
import os

from .env import get_db_connection_string

def init_db_session():
    db_connection_string = get_db_connection_string()
    engine = create_engine(db_connection_string, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session