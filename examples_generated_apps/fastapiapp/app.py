
# app.py
import os

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from collections.collection import Collection

# Database setup
DB_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize FastAPI
app = FastAPI()


# Routes
@app.get("/collections")
def get_collections():
    session = SessionLocal()
    try:
        collections = session.query(Collection).all()
        data = [collection.dict() for collection in collections]
        return data
    finally:
        session.close()


@app.post("/collections")
def add_collection(collection: Collection):
    session = SessionLocal()
    try:
        session.add(collection)
        session.commit()
        return collection.dict()
    finally:
        session.close()


# Create tables
Base.metadata.create_all(bind=engine)