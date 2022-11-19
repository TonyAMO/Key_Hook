from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship
from orm_base import Base


class room_requests(Base):
    __tablename__= "room_requests"
    employee_id = Column(Integer, ForeignKey('employees.emp_ID'), nullable=False, primary_key=True, unique=True)
    room_number = Column(Integer, nullable=False, primary_key=True, unique=True)
    building_name = Column(String(5), nullable=False, primary_key=True)
    request_date = Column('request_date', Date, nullable=False)

    __table_args__0 = (UniqueConstraint('employee_id', 'room_number', name='rr_uk_01'), )

    __table_args__ = (ForeignKeyConstraint(['room_number', 'building_name'],
                                            ['rooms.number', 'rooms.building_name']), {})

    #table_args = (UniqueConstraint('employee_id', 'room_number', 'building_name', name='rr_uk_01'))

    key_issue = relationship("key_issues", back_populates='room_requests', uselist=False)

    def __init__(self, date:Date, room, employee):
        self.employee_id=employee.emp_ID
        self.room_number=room.number
        self.building_name=room.building_name
        self.request_date=date