from config.database import Base
from sqlalchemy import Column, Integer, String

#definicion del modelo Team

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    founded = Column(Integer)
    country = Column(String)
    stadium = Column(String)
    coach = Column(String)