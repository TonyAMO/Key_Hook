from sqlalchemy import Column, String, Integer, Identity, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access import access

class doors(Base):
    __tablename__='doors'
    # door_id = Column('request_id', Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)
    door_name = Column(String(20), ForeignKey('door_formats.name'), nullable=False, unique=True)
    room_number = Column(Integer, nullable=False, primary_key=True, unique=True)
    building_name = Column(String(5), nullable=False, primary_key=True, unique=True)
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), nullable=False)

    #table_args = (UniqueConstraint('door_name', 'room_number', 'building_name', name='doors_uk_01'),)

    __table_agrs__ = (ForeignKeyConstraint([room_number, building_name],['rooms.number', 'rooms.building_name']),{})

    hook_list:[access] = relationship('access', back_populates='door', viewonly=False)

    def __init__(self, dn:String, rn:String, bn:String):
        self.door_name=dn
        self.room_number=rn
        self.building_name=bn