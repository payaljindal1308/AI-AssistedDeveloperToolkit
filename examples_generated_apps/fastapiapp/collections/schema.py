
# collections/schema.py
from typing import List
from pydantic import BaseModel

class Collection(BaseModel):
    id: int
    title: str
    image: str

class CollectionCreate(BaseModel):
    title: str
    image: str

class CollectionUpdate(BaseModel):
    title: str
    image: str

class CollectionOut(BaseModel):
    id: int
    title: str
    image: str

class CollectionList(BaseModel):
    collections: List[CollectionOut]