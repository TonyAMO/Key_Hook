from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests

class key_issues(Base):
    __tablename__='key_issues'
    issue_time = Column('issue_time', Time, nullable=False, primary_key=True, unique=True)
    issue_date = Column('issue_date', Date, nullable=False, primary_key=True, unique=True)
    employee_id = Column(Integer, ForeignKey('employees.emp_ID'), nullable=False, primary_key=True, unique=True)
    keys_number = Column(Integer, ForeignKey('keys.serial_number'), nullable=False, primary_key=True, unique=True)
    building_name = Column(String(5), nullable=False)
    room_number = Column(Integer, nullable=False)

    __table_args__ = (ForeignKeyConstraint(['building_name','room_number'],
                                           ['room_requests.building_name', 'room_requests.room_number']),{})

    #table_args = (UniqueConstraint('employee_id', 'keys_number', 'issue_time', 'issue_date', name='ki_uk_01'))

    # employee = relationship("employees", back_populates='keys')
    # key = relationship("keys", back_populates='employees')
    room_request = relationship("room_requests", back_populates="key_issues")

    def __init__(self, time:Time, date:Date, employee, key, room_request):
        self.issue_time=time
        self.issue_date=date
        self.employee_id=employee.emp_ID
        self.keys_number=key.serial_number
        self.building_name=room_request.building_name
        self.room_number=room_request.room_number