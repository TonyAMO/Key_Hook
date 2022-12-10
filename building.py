from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base

class building(Base):
    __tablename__='building'
    name = Column('name', String(5), nullable=False, primary_key=True)

    room = relationship('rooms')

    def __init__(self, name:String):
        self.name=name

    def __str__(self):
        return self.name