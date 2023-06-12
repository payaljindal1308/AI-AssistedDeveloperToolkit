
import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# Create an instance of FastAPI
app = FastAPI()

# Get the Database Connection String from Environment Variable
db_string = os.getenv('DATABASE_CONNECTION_STRING')

# Create Engine
engine = create_engine(db_string)

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Get Endpoint
@app.get("/collection")
def get_collection():
    collection = session.execute("SELECT * FROM collection")
    return collection

# Post Endpoint
@app.post("/collection")
def post_collection(title: str, image: str):
    session.execute("INSERT INTO collection (title, image) VALUES (:title, :image)", {'title':title, 'image':image})
    session.commit()
    return {'message': 'Successfully added to collection'}