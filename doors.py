from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access import access

class doors(Base):
    __tablename__='doors'
    door_name = Column(String(20), ForeignKey('door_formats.name'), nullable=False, unique=True)
    room_number = Column(Integer, ForeignKey('rooms.number'), nullable=False, primary_key=True, unique=True)
    building_name = Column(String(5), ForeignKey('rooms.building_name'), nullable=False, primary_key=True, unique=True)

    table_args = (UniqueConstraint('door_name', 'room_number', 'building_name', name='doors_uk_01'),)

    hook_list:[access] = relationship('access', back_populates='doors', viewonly=False)

    def __init__(self, dn:String, rn:String, bn:String):
        self.door_name=dn
        self.room_number=rn
        self.building_name=bn