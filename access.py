from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

class access(Base):
    __tablename__= 'access'
    # door_id = Column(Integer, nullable=False, primary_key=True)
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), nullable=False, primary_key=True)
    room_number = Column(Integer, nullable=False, primary_key=True)
    building_name = Column(String(5), nullable=False, primary_key=True)

    # __tableargs__ = (ForeignKeyConstraint([door_id, room_number, building_name],
    #                                       ['doors.door_if', 'doors.room_number', 'doors.building_name']),{})

    __tableargs__ = (ForeignKeyConstraint([room_number, building_name],
                                          ['doors.room_number', 'doors.building_name']), {})

    door = relationship('doors', back_populates='hook_list')
    hook = relationship('hooks', back_populates='door_list')

    def __init__(self, door, hook):
        self.door_id=door.door_id
        self.hook_id=hook.hook_id
        self.room_number=door.room_number
        self.building_name=door.building_name