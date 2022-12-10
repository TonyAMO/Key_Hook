from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, UniqueConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests

class rooms(Base):
    __tablename__='rooms'
    number = Column('number', Integer, nullable=False, primary_key=True)
    building_name = Column(String(5), nullable=False, primary_key=True)

    table_args = (ForeignKeyConstraint([building_name],['building.name'],{}))
    table_args1 = (UniqueConstraint(number, building_name, name='rooms_uk_01'))

    # door = relationship('doors')
    # build = relationship("building", back_populates="room")

    def __init__(self, num:Integer, bn:String):
        self.number=num
        self.building_name=bn



    def __str__(self):
        return "Room: {building_name} {room_number}".format(building_name = self.building_name, room_number=self.number)