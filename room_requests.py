from sqlalchemy import Column, String, Integer, Identity, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import date



class room_requests(Base):
    __tablename__= "room_requests"
    request_id = Column('request_id', Integer, Identity(start=1, cycle=True), nullable=False)
    request_date = Column('request_date', Date, nullable=False,primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False, primary_key=True)
    room_number = Column(Integer, nullable=False, primary_key=True)
    building_name = Column(String(5), nullable=False, primary_key=True)


    __table_args__ = (ForeignKeyConstraint([room_number, building_name],
                                            ['rooms.number', 'rooms.building_name']), {})

#orders = relationship("Order") #
#customer: Customer = relationship("Customer", back_populates="orders")
#               customer_id = Column('customer_id', Integer, ForeignKey('customers.customer_id'),
       #         primary_key=True, nullable=False)


    key_issue = relationship("key_issues", back_populates='room_request')
    room = relationship("rooms", back_populates='employee_list')
    employee = relationship("employees", back_populates='room_list')

    def __init__(self,  employee, room):
        self.employee_id=employee.id
        self.room_number=room.number
        self.building_name=room.building_name
        self.request_date=date.today()
        self.employee=employee
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
