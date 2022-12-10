from sqlalchemy import Column, Sequence, String, Identity, UniqueConstraint, Integer, ForeignKey, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from key_issues import key_issues

class keys(Base):
    __tablename__ = "keys"
    key_number = Column('key_number', Integer,Identity(start=100, cycle=True), nullable=False, primary_key=True)
    hook_id = Column(ForeignKey('hooks.hook_id'), nullable=False)

    table_args = (UniqueConstraint(key_number, hook_id, name="keys_uk_01"),)

    employee_list: [key_issues] = relationship('key_issues', back_populates='key')

    def __init__(self, hid:Integer):
         self.hook_id=hid

    def __str__(self):
        return "Key: {key_number}, Hook: {}".format(key_number = self.serial_number, hook_id=self.hook_id)