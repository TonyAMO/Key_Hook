from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access import access

class hooks(Base):
    __tablename__='hooks'
    hook_id = Column('hook_id', Integer, nullable=False, primary_key=True)

    key = relationship('keys')
    doors_list: [access] = relationship('access', back_populates='hooks', viewonly=False)

    def __init__(self, hi:Integer):
        self.hook_id=hi