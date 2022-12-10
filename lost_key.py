from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import *


class lost_key(Base):
    __tablename__ = 'lost_key'
    lost_date = Column('lost_date', Date, nullable=False, primary_key=True)
    key_number = Column(Integer, nullable=False,primary_key=True)
    employee_id = Column(Integer, nullable=False, primary_key=True)


    table_args = (ForeignKeyConstraint([key_number, employee_id],['key_issues.key_number', 'key_issues.employee_id']),{})

    #issue = relationship("key_issues", back_populates="lost_key")

    def __init__(self, kid, eid):
        self.lost_date=date.today()
        self.key_number = kid
        self.employee_id = eid