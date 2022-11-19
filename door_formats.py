from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base

class door_formats(Base):
    __tablename__='door_formats'
    name = Column('name', String(20), nullable=False, primary_key=True)

    def __init__(self, dfn:String):
        self.name=dfn