from sqlalchemy import Column, String, Integer, Identity, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access import access

class doors(Base):
    __tablename__='doors'
    door_id = Column('door_id', Integer, Identity(start=100, cycle=True), nullable=False, primary_key=True)
    door_name = Column(String(20), nullable=False)
    room_number = Column(Integer, nullable=False, primary_key=True)
    building_name = Column(String(5), nullable=False, primary_key=True)

    table_args = (UniqueConstraint(door_name, room_number, building_name, name='doors_uk_01'),)
    table_agrs1 = (ForeignKeyConstraint([room_number, building_name],['rooms.number', 'rooms.building_name']),{})
    table_agrs2 = (ForeignKeyConstraint([door_name], ['door_formats.name']),{})

    hook_list:[access] = relationship('access', back_populates='door')

    def __init__(self, room, dn:String):
        self.door_name=dn
        self.room_number=room.number
        self.building_name=room.building_name
        self.room=room
