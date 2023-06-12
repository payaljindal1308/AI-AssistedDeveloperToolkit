
import os
import json
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Collection

# Get the database connection string from environment variable
db_url = os.environ.get(DATABASE_URL)

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Create a FastAPI instance
app = FastAPI()


@app.get("/data")
def get_data():
    """
    Get data from the collections table
    """
    # Create a session
    session = Session()

    # Get all the data from the collections table
    data = session.query(Collection).all()

    # Convert the data to a list of dictionaries
    data = [item.to_dict() for item in data]

    # Close the session
    session.close()

    # Return the data
    return json.dumps(data)


@app.post("/data")
def post_data(data):
    """
    Post data to the collections table
    """
    # Create a session
    session = Session()

    # Create a collection object
    collection = Collection(**data)

    # Add the collection object to the session
    session.add(collection)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()

    # Return a success message
    return {"message": "data added successfully"}