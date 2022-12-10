from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import *

class returned_key(Base):
    __tablename__='returned_key'
    return_date = Column('return_date',Date, primary_key=True, nullable=False)
    key_number = Column(Integer, primary_key=True, nullable=False)
    employee_id = Column(Integer, primary_key=True, nullable=False)


    __table_args__ = (ForeignKeyConstraint([key_number, employee_id],['key_issues.key_number', 'key_issues.employee_id']),{})

   # issue = relationship("key_issues", back_populates="returned_key")


    def __init__(self, kid, eid):
        self.issue_date = date.today()
        self.key_number = kid
        self.employee_id = eid