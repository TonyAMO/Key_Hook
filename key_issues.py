from sqlalchemy import Column, String, Sequence, Integer, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests
from datetime import *
import time

class key_issues(Base):
    __tablename__='key_issues'
    issue_time = Column('issue_time', Time, nullable=False)
    issue_date = Column('issue_date', Date, nullable=False)
    key_number = Column(ForeignKey('keys.serial_number'), primary_key=True)
    request_id = Column(ForeignKey('room_requests.request_id'), nullable=False)
    employee_id = Column(ForeignKey('employees.id'), nullable=False, primary_key=True)



    #table_args = (UniqueConstraint('employee_id', 'keys_number', 'issue_time', 'issue_date', name='ki_uk_01'))

    employee = relationship("employees", back_populates='key_list')
    key = relationship("keys", back_populates='employee_list')

    #room_request: room_requests = relationship("room_requests", back_populates="key_issue")

    room_request = relationship("room_requests", back_populates="key_issue")

    def __init__(self, rr, key):
        self.issue_time=datetime.now()
        self.issue_date=date.today()
        self.key_number = key.serial_number
        self.employee_id=rr.employee_id
        self.room_request=rr
