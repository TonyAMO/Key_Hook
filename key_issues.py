from sqlalchemy import Column, String, Sequence, Integer, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import *

class key_issues(Base):
    __tablename__='key_issues'
    issue_date = Column('issue_date', Date, nullable=False)
    key_number = Column(Integer, primary_key=True, nullable=False)
    request_id = Column(Integer, nullable=False)
    employee_id = Column(Integer, primary_key=True, nullable=False)

    table_args = (UniqueConstraint(issue_date,employee_id,  name='ki_uk_01'),)
    table_args1 = (ForeignKeyConstraint([key_number],['keys.key_number']),{})
    table_args2 = (ForeignKeyConstraint([employee_id], ['employees.id']),{})
    table_args3 = (ForeignKeyConstraint([request_id], ['room_requests.request_id']),{})

    employee = relationship("employees", back_populates='key_list')
    key = relationship("keys", back_populates='employee_list')

    #room_request: room_requests = relationship("room_requests", back_populates="key_issue")

    #room_request = relationship("room_requests", back_populates="key_issue")

    def __init__(self, rid, eid, key):
        self.issue_time=datetime.now()
        self.issue_date=date.today()
        self.key_number = key.serial_number
        self.request_id = rid
        self.employee_id=eid

