
# endpoints/__init__.py
import os
from fastapi import FastAPI
from models import Collection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from endpoints.get_data import get_data
from endpoints.post_data import post_data

# Get Database Connection String from environment variable
DATABASE_URL = os.environ['DATABASE_URL']

# Database setup
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Initialize FastAPI
app = FastAPI()

# Add endpoints
app.add_api_route('/get_data', get_data, methods=['GET'])
app.add_api_route('/post_data', post_data, methods=['POST'])