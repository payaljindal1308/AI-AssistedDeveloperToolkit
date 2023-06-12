
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database Connection String 
db_string = os.getenv('DB_CONNECTION_STRING')

# Create Engine
engine = create_engine(db_string)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()