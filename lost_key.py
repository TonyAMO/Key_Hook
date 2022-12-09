from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base


class lost_key(Base):
    __tablename__ = 'lost_key'
    key_number = Column(Integer, primary_key=True)
    lost_date = Column('lost_date', Date, nullable=False, primary_key=True)

    employee_id = Column(Integer, nullable=False, primary_key=True)

    # __table_args__ = (ForeignKeyConstraint([key_number, request_date, employee_id, building_name, room_number],
    #                                        ['key_issues.key_number',
    #                                         'key_issues.request_date', 'key_issues.employee_id',
    #                                         'key_issues.building_name', 'key_issues.room_number']), {})

    __table_args__ = (ForeignKeyConstraint([key_number, employee_id],
                                           ['key_issues.key_number', 'key_issues.employee_id']), {})

    #issue = relationship("key_issues", back_populates="lost_key")

    def __init__(self, issue):
        self.key_number = issue.key_number
        self.employee_id = issue.employee_id