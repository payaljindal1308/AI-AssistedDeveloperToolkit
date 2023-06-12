
import os
import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from models import Collection
from utils.db import get_db

app = FastAPI()

# Get data from postgres database
@app.get("/data")
def get_data():
    session = get_db()
    collections = session.query(Collection).all()
    return collections
 
# Post data to postgres database
@app.post("/data")
def post_data(collection: Collection):
    session = get_db()
    session.add(collection)
    session.commit()
    return collection