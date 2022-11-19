from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests
from key_issues import key_issues

class employees(Base):
    __tablename__='employees'
    emp_ID = Column('emp_ID', Integer, nullable=False, primary_key=True)
    name = Column('name', String(50), nullable=False)
    fine = Column('fine', DECIMAL(10, 2), nullable=False)

    key_list:[key_issues] = relationship('key_issues', back_populates='rooms', viewonly=False)
    doors_list:[room_requests] = relationship('room_requests', back_populates='employees', viewonly=False)

    def __init__(self, id:Integer, n:String, f:DECIMAL(10,2)):
        self.emp_ID=id
        self.name=n
        self.fine=f