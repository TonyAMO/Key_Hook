from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base

class returned_key(Base):
    __tablename__='returned_key'
    issue_time = Column(Time, ForeignKey('key_issues.issue_time'),nullable=False, primary_key=True)
    issue_date = Column(Date, ForeignKey('key_issues.issue_date'), nullable=False, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.emp_ID'), nullable=False, primary_key=True)
    keys_number = Column(Integer, ForeignKey('keys.serial_number'), nullable=False, primary_key=True)

   # issue = relationship("key_issues", back_populates="returned_key")

    def __init__(self, issue):
        self.issue_time=issue.issue_time
        self.issue_date = issue.issue_date
        self.employee_id = issue.employee_id
        self.keys_number = issue.keys_number