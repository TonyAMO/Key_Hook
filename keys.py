from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from key_issues import key_issues

class keys(Base):
    __tablename__ = "keys"
    serial_number = Column('serial_number', Integer, nullable=False, primary_key=True)
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), nullable=False)

    employee_list:[key_issues] = relationship('key_issues', back_populates='keys', viewonly=False)

    def __init__(self, sn:Integer, hook):
        self.serial_number=sn
        self.hook_id=hook.hook_id