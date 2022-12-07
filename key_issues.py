from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from room_requests import room_requests
from datetime import *
import time

class key_issues(Base):
    __tablename__='key_issues'
    issue_time = Column('issue_time', Time, nullable=False)
    issue_date = Column('issue_date', Date, nullable=False)
    key_number = Column(Integer, ForeignKey('keys.serial_number'), nullable=False, primary_key=True)
    request_date = Column(Date, nullable=False, primary_key=True)
    employee_id = Column(Integer, nullable=False, primary_key=True)
    building_name = Column(String(5), nullable=False, primary_key=True)
    room_number = Column(Integer, nullable=False, primary_key=True)


    __table_args__ = (ForeignKeyConstraint([request_date, employee_id, building_name,room_number],
                        ['room_requests.request_date','room_requests.employee_id',
                         'room_requests.building_name', 'room_requests.room_number']), {})

    #table_args = (UniqueConstraint('employee_id', 'keys_number', 'issue_time', 'issue_date', name='ki_uk_01'))

    # employee = relationship("employees", back_populates='keys')

    #room_request: room_requests = relationship("room_requests", back_populates="key_issue")

    room_request = relationship("room_requests", back_populates="key_issue")

    def __init__(self, rr, key):
        self.issue_time=datetime.now()
        self.issue_date=date.today()
        self.key_number = key.serial_number
        self.request_date=rr.request_date
        self.employee_id=rr.employee_id
        self.building_name=rr.building_name
        self.room_number=rr.room_number
        self.room_request=rr
