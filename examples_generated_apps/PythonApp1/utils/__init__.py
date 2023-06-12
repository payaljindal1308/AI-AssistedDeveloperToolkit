
# utils/__init__.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = os.getenv('DATABASE_CONNECTION_STRING')
engine = create_engine(db_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()