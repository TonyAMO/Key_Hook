from sqlalchemy import Column, String, Sequence, Integer, Identity, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import date



class room_requests(Base):
    __tablename__= "room_requests"
    request_id = Column('request_id', Integer,Identity(start=1000, cycle=True), nullable=False, primary_key=True)
    request_date = Column('request_date', Date, nullable=False)
    employee_id = Column(Integer, nullable=False)
    room_number = Column(Integer, nullable=False)
    building_name = Column(String(5), nullable=False)

    table_args2 = (UniqueConstraint(request_date, employee_id, room_number, building_name, name="rr_uk_01"),)
    table_args = (ForeignKeyConstraint([room_number, building_name], ['rooms.number', 'rooms.building_name']),{})
    table_args1 = (ForeignKeyConstraint([employee_id],['employees.id']),{})



    key_issue = relationship("key_issues", back_populates='room_request') #one-to-one with key_issues
    # room = relationship("rooms", back_populates='employee_list')
    # employee = relationship("employees", back_populates='room_list')

    def __init__(self,  id:Integer, room):
        self.employee_id=id
        self.room_number=room.number
        self.building_name=room.building_name
        self.request_date=date.today()
        self.room=room

    # def add_key(self, key):
    #     for next_key in self.key_list:
    #         if next_key == key:
    #             return
    #     # Create an instance of the junction table class.
    #     ki = key_issues(key, self)
    #     # add that new instance to the list of genres that the Movie keeps.
    #     key.request_key.append(ki)
    #     # add that new instance to the list of movies that this genre keeps.
    #     self.key_list.append(ki)
