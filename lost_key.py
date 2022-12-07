from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, Time, Date
from sqlalchemy.orm import relationship
from orm_base import Base


class lost_key(Base):
    __tablename__ = 'lost_key'
    key_number = Column(Integer, nullable=False)
    request_date = Column(Date, nullable=False, primary_key=True)
    employee_id = Column(Integer, nullable=False, primary_key=True)
    building_name = Column(String(5), nullable=False, primary_key=True)
    room_number = Column(Integer, nullable=False, primary_key=True)

    __table_args__ = (ForeignKeyConstraint([key_number, request_date, employee_id, building_name, room_number],
                                           ['key_issues.key_number',
                                            'key_issues.request_date', 'key_issues.employee_id',
                                            'key_issues.building_name', 'key_issues.room_number']), {})

    #issue = relationship("key_issues", back_populates="lost_key")

    def __init__(self, issue):
        self.key_number = issue.key_number
        self.request_date = issue.request_date
        self.employee_id = issue.employee_id
        self.building_name = issue.building_name
        self.room_number = issue.room_number