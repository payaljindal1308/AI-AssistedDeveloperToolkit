
from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    image = Column(String)