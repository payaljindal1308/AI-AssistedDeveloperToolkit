
# collections/collection.py
import sqlalchemy
from sqlalchemy import Column, Integer, String
from collections.config import Base

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    image = Column(String(255))