
# utils/db.py
import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get database connection string from environment variable
DATABASE_URL = os.environ.get('DATABASE_URL')

# Create an engine that stores data in the local directory's
engine = create_engine(DATABASE_URL)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
# Table Name: collections
# Table fields: id, title, image
metadata = sqlalchemy.MetaData()
collections = sqlalchemy.Table('collections', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('title', sqlalchemy.String),
    sqlalchemy.Column('image', sqlalchemy.String)
)
metadata.create_all(engine)

# Create a sessionmaker object to establish a link of communication between
# our code executions and the engine we just created
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()