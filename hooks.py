from sqlalchemy import Column, Sequence, String, Identity, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access import access

class hooks(Base):
    __tablename__='hooks'
    hook_id = Column('hook_id', Integer, primary_key=True)

    # key = relationship('keys')
    door_list: [access] = relationship('access', back_populates='hook', viewonly=False)

    # def __init__(self, hi:Integer):
    #      self.hook_id=hi

    def __str__(self):
        return "Hook: "+ f'{self.hook_id}'