
main.py
import os
import uvicorn
from fastapi import FastAPI

from app.db.session import Session
from app.models.collection import Collection
from app.routers import collections

app = FastAPI()

# Get DB connection string from environment variable
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

# Create the Session object
session = Session(DB_CONNECTION_STRING)

# Register the router
app.include_router(collections.router, prefix="/collections", tags=["collections"])

@app.on_event("startup")
async def startup():
    # Create the tables if they don't exist
    Collection.metadata.create_all(session.engine)

@app.on_event("shutdown")
async def shutdown():
    # Close the session
    session.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)