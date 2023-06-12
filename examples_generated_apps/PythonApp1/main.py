
# main.py
import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Collection
from routes import router
from config import settings

# Create Database engine
db_string = os.environ.get('DATABASE_CONNECTION_STRING')
engine = create_engine(db_string)
Base.metadata.create_all(engine)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

# Create FastAPI App
app = FastAPI()

# Register Routes
app.include_router(router)