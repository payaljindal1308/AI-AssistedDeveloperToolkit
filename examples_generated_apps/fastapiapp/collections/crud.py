
# collections/crud.py

from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Collection

router = APIRouter()

engine = create_engine('sqlite:///collections.db')
Base.metadata.create_all(engine)

@router.get("/collection/{id}")
def get_collection(id: int):
    session = Session(bind=engine)
    collection = session.query(Collection).filter(Collection.id == id).first()
    session.close()
    return collection

@router.post("/collection")
def create_collection(title: str, image: str):
    session = Session(bind=engine)
    collection = Collection(title=title, image=image)
    session.add(collection)
    session.commit()
    session.close()
    return collection