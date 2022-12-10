from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

class access(Base):
    __tablename__= 'access'
    # door_id = Column(Integer, nullable=False, primary_key=True)
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), nullable=False, primary_key=True)
    door_id = Column(Integer, ForeignKey('doors.door_id'), nullable=False, primary_key=True)


    table_args = (UniqueConstraint(hook_id, door_id, name="access_uk_01"))

    door = relationship('doors', back_populates='hook_list')
    hook = relationship('hooks', back_populates='door_list')

    def __init__(self, door, hid):
        self.door_id=door.door_id
        self.hook_id=hid