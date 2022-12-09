from sqlalchemy import Column, Sequence, String, Integer, ForeignKey, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from key_issues import key_issues

class keys(Base):
    __tablename__ = "keys"
    serial_number = Column('serial_number', Integer, primary_key=True)
    hook_id = Column(ForeignKey('hooks.hook_id'), nullable=False)

    employee_list: [key_issues] = relationship('key_issues', back_populates='key', viewonly=False)

    # def __init__(self, hook):
    #     self.hook_id=hook.hook_id
        #self.request_key=[]

    # def add_request(self, request):
    #     for next_request in self.request_key:
    #         if next_request == request:
    #             return
    #     # Create an instance of the junction table class.
    #     ki = key_issues(request, self)
    #     # add that new instance to the list of genres that the Movie keeps.
    #     request.key_list.append(ki)
    #     # add that new instance to the list of movies that this genre keeps.
    #     self.request_key.append(ki)

    def __str__(self):
        return "Key: {key_number}, Hook: {}".format(key_number = self.serial_number, hook_id=self.hook_id)