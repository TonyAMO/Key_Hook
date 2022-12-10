from sqlalchemy import Column, Sequence, String, Identity, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access import access


class hooks(Base):
    __tablename__='hooks'
    hook_id = Column('hook_id', Integer, Identity(start=1, cycle=True), nullable=False,primary_key=True)

    key = relationship('keys') #one-to-one with keys
    door_list: [access] = relationship('access', back_populates='hook')



    def __str__(self):
        return "Hook: "+ f'{self.hook_id}'