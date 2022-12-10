from sqlalchemy import Column, String, Sequence, Integer, DECIMAL, UniqueConstraint, ForeignKey, ForeignKeyConstraint, Time, Date, Identity
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests
from key_issues import key_issues

class employees(Base):
    __tablename__='employees'
    id = Column('id', Integer, Identity(start=1000, cycle=True),primary_key=True)
    name = Column('name', String(50), nullable=False)
    fine = Column('fine', DECIMAL(10, 2), nullable=False)


    key_list: [key_issues] = relationship('key_issues', back_populates='employee')

    def __init__(self, n:String, f:DECIMAL(10,2)):
        self.name=n
        self.fine=f


    def __str__(self):
        return "Employee: {emp_name} {fine_owed}".format(emp_name = self.name, fine_owed=self.fine)