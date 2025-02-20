from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Kohvikud(Base):
    __tablename__ = 'sookla'
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    operator = Column(String(100), nullable=False)
    time_open = Column(String(100), nullable=False)
    time_close = Column(String(100), nullable=False)
