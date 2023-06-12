
import os

# Get Database Connection String
DATABASE_CONNECTION_STRING = os.environ.get('DATABASE_CONNECTION_STRING')

# Create SQLAlchemy Session
from sqlalchemy import create_engine
engine = create_engine(DATABASE_CONNECTION_STRING)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Create FastAPI Server
from fastapi import FastAPI
app = FastAPI()

# Create GET Endpoint
@app.get("/collections")
def get_collections():
    collections = session.query(Collection).all()
    return collections

# Create POST Endpoint
@app.post("/collections")
def post_collection(title: str, image: str):
    collection = Collection(title=title, image=image)
    session.add(collection)
    session.commit()
    return collection