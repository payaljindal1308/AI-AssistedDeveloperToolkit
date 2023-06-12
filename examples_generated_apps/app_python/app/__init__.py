
# app/__init__.py
import os
from fastapi import FastAPI
from app.db.session import Session
from app.models.collection import Collection
from app.routers.collections import collections_router

app = FastAPI()

app.add_route("/collections", collections_router)

@app.on_event("startup")
async def startup():
    Session.bind = os.environ.get("DATABASE_URL")

@app.on_event("shutdown")
async def shutdown():
    Session.close()