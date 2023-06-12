
# models.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Get Database Connection String from Environment Variable
db_connection_string = os.getenv('DB_CONNECTION_STRING')

# Create Database Engine
engine = create_engine(db_connection_string)

# Create Database Session
Session = sessionmaker(bind=engine)

# Create Database Table
class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    image = Column(String)