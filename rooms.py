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
    build = relationship("building", back_populates="room")
    employee_list:[room_requests] = relationship('room_requests', back_populates='room', viewonly=False)

    def __init__(self, num:Integer, building):
        self.number=num
        self.building_name=building.name
        self.building=building
        self.employee_list=[]

    def add_employee(self, employee):
        # make sure this genre is non already on the list.
        for next_employee in self.employee_list:
            if next_employee == employee:
                return
        # Create an instance of the junction table class for this relationship.
        rr = room_requests(employee, self)
        # Update this move to reflect that we have this genre now.
        employee.room_list.append(rr)
        # Update the genre to reflect this movie.
        self.employee_list.append(rr)

    def __str__(self):
        return "Room: {building_name} {room_number}".format(building_name = self.building_name, room_number=self.number)