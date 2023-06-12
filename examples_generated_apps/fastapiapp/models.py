
# models.py
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

engine = create_engine('sqlite:///collections.db')
Base = declarative_base()

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    image = Column(Text)

Base.metadata.create_all(engine)