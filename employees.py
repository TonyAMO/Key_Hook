from sqlalchemy import Column, String, Integer, DECIMAL, UniqueConstraint, ForeignKey, ForeignKeyConstraint, Time, Date, Identity
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests
from key_issues import key_issues

class employees(Base):
    __tablename__='employees'
    id = Column('id', Integer, nullable=False, primary_key=True)
    name = Column('name', String(50), nullable=False)
    fine = Column('fine', DECIMAL(10, 2), nullable=False)


    room_list:[room_requests] = relationship('room_requests', back_populates='employee', viewonly=False)

    def __init__(self, id:Integer, n:String, f:DECIMAL(10,2)):
        self.id = id
        self.name=n
        self.fine=f
        self.room_list=[]

    def add_room(self, room):
        # make sure this genre is non already on the list.
        for next_room in self.room_list:
            if next_room == room:
                return
        # Create an instance of the junction table class for this relationship.
        rr = room_requests(room, self)
        # Update this move to reflect that we have this genre now.
        room.employee_list.append(rr)
        # Update the genre to reflect this movie.
        self.room_list.append(rr)

    def __str__(self):
        return "Employee: {emp_name} {fine_owed}".format(emp_name = self.name, fine_owed=self.fine)