from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, UniqueConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests

class rooms(Base):
    __tablename__='rooms'
    number = Column('number', Integer, nullable=False, primary_key=True, unique=True)
    building_name = Column(String(5), ForeignKey('building.name'), nullable=False, primary_key=True, unique=True)

    table_args = (UniqueConstraint('number', 'building_name', name='rooms_uk_01'))

    door = relationship('doors')
    employee_list:[room_requests] = relationship('room_requests', back_populates='rooms', viewonly=False)

    def __init__(self, num:Integer, bn:String):
        self.number=num
        self.building_name=bn