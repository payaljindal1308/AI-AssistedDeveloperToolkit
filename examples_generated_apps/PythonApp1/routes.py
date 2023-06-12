
import os
import models
from fastapi import FastAPI
from sqlalchemy.orm import Session
from config import DATABASE_URL

app = FastAPI()

@app.get("/")
def get_data(): 
    db_connection = os.getenv(DATABASE_URL)
    session = Session(db_connection)
    collection_data = session.query(models.Collection).all()
    return collection_data

@app.post("/")
def post_data(collection: models.Collection):
    db_connection = os.getenv(DATABASE_URL)
    session = Session(db_connection)
    session.add(collection)
    session.commit()
    return collection