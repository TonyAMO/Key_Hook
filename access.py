from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

class access(Base):
    __tablename__= 'access'
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), nullable=False, primary_key=True)
    room_number = Column(Integer, ForeignKey('doors.room_number'), nullable=False, primary_key=True)
    building_name = Column(String(5), ForeignKey('doors.building_name'), nullable=False, primary_key=True)

    # door = relationship('doors', back_populates='hooks')
    # hook = relationship('hooks', back_populates='doors')

    def __init__(self, door, hook):
        self.hook_id=hook.hook_id
        self.room_number=door.room_number
        self.building_name=door.building_name