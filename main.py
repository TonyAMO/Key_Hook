from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
from orm_base import metadata
import logging
from sqlalchemy.exc import IntegrityError
from keys import keys
from access import access
from building import building
from door_formats import door_formats
from doors import doors
from employees import employees
from hooks import hooks
from issued_key import issued_key
from key_issues import key_issues
from lost_key import lost_key
from returned_key import returned_key
from room_requests import room_requests
from rooms import rooms
from datetime import *


if __name__=='__main__':
    logging.basicConfig()
    # use the logging factory to create our first logger.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # use the logging factory to create our second logger.
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)
    
    metadata.drop_all(bind=engine)  # start with a clean slate while in development
    
    # Create whatever tables are called for by our "Entity" classes.  The simple fact that
    # your classes that are subtypes of Base have been loaded by Python has populated
    # the metadata object with their definition.  So now we tell SQLAlchemy to create
    # those tables for us.
    metadata.create_all(bind=engine)

    # b1: building = building('ECS')
    # r1: rooms = rooms(308, b1)
    # h1: hooks = hooks(12345)
    # k1: keys = keys(123456, h1)
    # e1: employees = employees(1234567, 'David Brown', 0.00)
    # rr1: room_requests = room_requests(e1,r1)
    # ki1: key_issues = key_issues(rr1,k1)
    # ik1: issued_key = issued_key(ki1)
    # lk1: lost_key = lost_key(ki1)

    with Session() as sess:
        # sess.begin()
        # sess.add(b1)
        # sess.add(r1)
        # sess.add(h1)
        # sess.add(k1)
        # sess.add(e1)
        # sess.add(rr1)
        # sess.add(ki1)
        # sess.commit()
        # sess.add(lk1)
        # sess.commit()
        #
        # buildings: [building] = sess.query(building).all()
        # print("here are the buildings")
        # for b in buildings:
        #     print(b)
        #
        # room: [rooms] = sess.query(rooms).all()
        # print("here are the rooms")
        # for r in room:
        #     print(r)
        #
        # key: [keys] = sess.query(keys).all()
        # print("here are the keys")
        # for k in key:
        #     print(k)
        #
        # employee: [employees] = sess.query(employees).all()
        # print("here are the employees")
        # for e in employee:
        #     print(e)
        #
        # sess.delete(e1)
        option = str(input('''Choose an option:
        \ta. Create a key
        \tb. Request access to a room
        \tc. Issue key to employee
        \td. Report lost key
        \te. Report all rooms that employee can enter given owned keys
        \tf. Delete a key
        \tg. Delete an employee
        \th. Add new door that can be opened by existing hook
        \ti. Update an access request to move it to new employee
        \tj. Report out all employees who can get into a room
        \n\nOption: '''))

        key_num = 0
        if option=='a':
            print("Creating a key")
            hook=0
            q = sess.query(hooks.hook_id).filter(hooks.hook_id==hook)
            while not sess.query(q.exists()).scalar():
                hook = int(input("\n\n\nValid hook ID to make a copy of: "))
                q = sess.query(hooks.hook_id).filter(hooks.hook_id==hook)
            key_num+=1
            newKey: keys = keys(serial_number=key_num,hook_id=hook)
            sess.add(newKey)
            sess.commit()
            print("\n\nNew Key("+f'{newKey.serial_number}'+") created")
        elif option=='b':
            print("Request access to room")
            empid=-1
            #check valid id
            q=sess.query(employees.id).filter(employees.id==empid)
            while not sess.query(q.exists()).scalar():
                empid=input("\n\n\nEnter valid employee ID: ")
                q = sess.query(employees.id).filter(employees.id == empid)
            bn=""
            #check valid building
            q = sess.query(building.name).filter(building.name == bn)
            while not sess.query(q.exists()).scalar():
                bu=(input("\n\n\nValid building access: ")).upper()
                q = sess.query(building.name).filter(building.name == bn)
            rn=-1
            #check valid room number
            q = sess.query(rooms.number).filter(rooms.number == rn)
            while not sess.query(q.exists()).scalar():
                rn=input("\n\n\nRoom number you want to access: ")
                q = sess.query(rooms.number).filter(rooms.number == rn)
            room: rooms=rooms(number=rn, building_name=bn)

            print("\nCreating room request...\n")
            request: room_requests=room_requests(employee=empid, room=room)
            sess.add(request)
            sess.commit()
        elif option=="c":
            print("Issue key to an employee")
            rr = -1
            #check valid id
            q = sess.query(room_requests.request_id).filter(room_requests.request_id == rr)
            while not sess.query(q.exists()).scalar():
                rr=int(input("\n\n\nEnter valid request ID: "))
                q = sess.query(room_requests.request_id).filter(room_requests.request_id == rr)
            request = sess.query(room_requests).filter(room_requests.request_id==rr).scalar()
            door = sess.query(doors).filter(doors.building_name==request.building_name,
                                            doors.room_number==request.room_number).scalar()
            acc = sess.query(access).filter(access.door_id==door.door_id).scalar()
            key = sess.query(keys).filter(room_requests.room_number==door.room_number,
                                          room_requests.building_name==door.building_name,
                                          keys.hook_id==acc.hook_id).scalar()
            print("\nIssuing key...\n")
            issue: issued_key = issued_key(request_id=rr, key=key)
            sess.add(issue)
            sess.commit()
            print("\nKey ("+f'{key.key_number}'+") issued to employee ID: "+f'{issue.employee_id}'
                  +"at "+f'{issue.request_date}'+"\n")
        elif option=="d":
            print("\n\n\nReport lost key")
            empid = -1
            #check valid id
            q = sess.query(issued_key.employee_id).filter(issued_key.employee_id==empid)
            while not sess.query(q.exists()).scalar():
                empid = int(input("\n\n\nEnter valid ID issued: "))
                q = sess.query(issued_key.employee_id).filter(issued_key.employee_id == empid)
            keyid = -1
            q = sess.query(issued_key.key_number).filter(issued_key.key_number == keyid)
            while not sess.query(q.exists()).scalar():
                empid = int(input("\n\n\nEnter valid ID issued: "))
                q = sess.query(issued_key.key_number).filter(issued_key.key_number == keyid)
            print("\nReporting key as lost...\n")
            lost: lost_key = lost_key()
        else:
            print('Choose another option')