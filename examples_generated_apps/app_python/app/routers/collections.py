

# app/routers/collections.py
import os

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.models.collection import Collection
from app.db.session import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    try:
        db_url = os.environ.get('DATABASE_URL')
        db = SessionLocal(db_url)
        yield db
    finally:
        db.close()

# GET endpoint
@router.get("/")
def get_collections(db: Session = Depends(get_db)):
    collections = db.query(Collection).all()
    return collections

# POST endpoint
@router.post("/")
def create_collection(collection: Collection, db: Session = Depends(get_db)):
    db.add(collection)
    db.commit()
    db.refresh(collection)
    return collection