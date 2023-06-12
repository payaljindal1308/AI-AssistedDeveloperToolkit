
# app/db/session.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database Connection string from environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create an engine that stores data in the local directory's
engine = create_engine(DATABASE_URL)

# Create a 'Session' class that establishes connections to the database
Session = sessionmaker(bind=engine)