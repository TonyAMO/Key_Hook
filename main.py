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

    b1: building = building('ECS')
    r1: rooms = rooms(308, )
    h1: hooks = hooks()
    # k1: keys = keys(123456, h1)
    e1: employees = employees('David Brown', 0.00)
    # rr1: room_requests = room_requests(e1,r1)
    # ki1: key_issues = key_issues(rr1,k1)
    # ik1: issued_key = issued_key(ki1)
    # lk1: lost_key = lost_key(ki1)

    with Session() as sess:
        # sess.begin()
        sess.add(b1)
        sess.add(r1)
        sess.add(h1)
        # sess.add(k1)
        sess.add(e1)
        # sess.add(rr1)
        # sess.add(ki1)
        #sess.commit()
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

        option = ""
        while option!="q":
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
            \tq. Quit
            \n\nOption: '''))


            if option=='a':
                print("Creating a key")
                hook=0
                q = sess.query(hooks.hook_id).filter(hooks.hook_id==hook)
                while not sess.query(q.exists()).scalar():
                    hook = int(input("\n\n\nValid hook ID to make a copy of: "))
                    q = sess.query(hooks.hook_id).filter(hooks.hook_id == hook)
                newKey: keys = keys(hook_id=hook)
                sess.add(newKey)
                sess.commit()
                print("\n\nNew Key("+f'{newKey.serial_number}'+") created")

            elif option=='b':
                print("Request access to room")
                empid=0
                #check valid id
                q=sess.query(employees.id).filter(employees.id==empid)
                while not sess.query(q.exists()).scalar():
                    empid=input("\n\n\nEnter valid employee ID: ")
                    q = sess.query(employees.id).filter(employees.id == empid)
                bn=""
                #check valid building
                q = sess.query(building.name).filter(building.name == bn)
                while not sess.query(q.exists()).scalar():
                    bn=(input("\n\n\nValid building you want to access: ")).upper()
                    q = sess.query(building.name).filter(building.name == bn)
                rn=-1
                #check valid room number
                q = sess.query(rooms.number).filter(rooms.number == rn)
                while not sess.query(q.exists()).scalar():
                    rn=input("\n\n\nRoom number you want to access: ")
                    q = sess.query(rooms.number).filter(rooms.number == rn)
                rom: rooms = rooms(num=rn, nam=bn)
                print("\nCreating room request...\n")
                request: room_requests=room_requests(empid, rom)
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
                issue: key_issues = key_issues(request_id=rr, key=key)
                sess.add(issue)
                sess.commit()
                print("\nKey ("+f'{key.key_number}'+") issued to employee ID: "+f'{issue.employee_id}'
                      +"at "+f'{issue.request_date}'+"\n")

            elif option=="d":
                print("\n\n\nReport lost key")
                empid = -1
                #check valid id
                q = sess.query(key_issues.employee_id).filter(key_issues.employee_id==empid)
                while not sess.query(q.exists()).scalar():
                    empid = int(input("\n\n\nEnter valid ID issued: "))
                    q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
                keyid = -1
                q = sess.query(key_issues.key_number).filter(key_issues.key_number == keyid)
                while not sess.query(q.exists()).scalar():
                    keyd = int(input("\n\n\nEnter valid key ID issued to employee: "))
                    q = sess.query(key_issues.key_number).filter(key_issues.key_number == keyid)
                print("\nReporting key as lost...\n")
                lost: lost_key = lost_key()
                sess.add(lost)
                sess.commit()
                print("\nKey "+f'{keyid}'+" Reported lost at: "+f'{lost.request_date}'), print()
                updt = sess.update(employees).where(employees.id==empid).values(fine=employees.fine+25)
                engine.execute(updt)
                print(f'{empid}'+" was fined $25")

            elif option=="e":
                print("Report out all the rooms an employee can enter given the keys they already have")
                empid = -1
                q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
                while not sess.query(q.exists()).scalar():
                    empid = int(input("\n\n\nEnter valid employee ID: "))
                    q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
                request_list = sess.query(key_issues.employee_id).filter(key_issues.employee_id==empid).all()
                request_list = [employee_id for employee_id, in request_list]
                result = sess.query(room_requests.room_number).filter(room_requests.request_id.in_(request_list)).all()
                print("\nEmployee "+f'{empid}'+" has access to rooms: "+f'{result}')

            elif option=="f":
                print("Delete a key")
                kid = int(input("\n\n\nEnter valid key ID to delete: "))
                try:
                    delete_lost = sess.query(lost_key).filter(lost_key.key_number==kid).all()
                    for obj in delete_lost:
                        sess.delete(obj)
                except:
                    print("No key was found")
                try:
                    delete_issued = sess.query(key_issues).filter(key_issues.key_number==kid).all()
                except:
                    print("No key was found")
                delete_user = sess.query(keys).filter(keys.serial_number==kid).all()
                for obj in delete_user:
                    sess.delete(obj)
                sess.commit()
                print("\nKey deleted")

            elif option=="g":
                print("Delete an employee")
                empid = -1
                q = sess.query(key_issues.employee_id).filter(key_issues.employee_id==empid)
                while not sess.query(q.exists()).scalar():
                    empid = int(input("\n\n\nEnter valid employee ID: "))
                    q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
                #delete employee in lost key
                d_emp_lost = sess.query(lost_key).filter(lost_key.employee_id==empid).all()
                for obj in d_emp_lost:
                    sess.delete(obj)
                    print("Deleted employee in lost key")
                #delete employee in issued key
                d_emp_iss = sess.query(key_issues).filter(key_issues.employee_id==empid).all()
                for obj in d_emp_iss:
                    sess.delete(obj)
                    print("Deleted employee in issued key")
                #delete employee in room request
                d_emp_rr = sess.query(room_requests).filter(room_requests.employee_id==empid).all()
                for obj in d_emp_rr:
                    sess.delete(obj)
                    print("Deleted employee in room request")
                #delete employee in employee
                d_emp = sess.query(employees).filter(employees.id == empid).all()
                for obj in d_emp:
                    sess.delete(obj)
                    print("Deleted employee")
                sess.commit()

            elif option=="h":
                print("add a new door that can be opened by existing hook")
                building_name=""
                #cehck valid building
                q = sess.query(building.name).filter(building.name==building_name)
                while not sess.query(q.exists()).scalar():
                    building_name=input("\nWhat is the building name?").upper()
                    q = sess.query(building.name).filter(building.name == building_name)
                room_number = -1
                q = sess.query(rooms.number).filter(rooms.number == room_number)
                while not sess.query(q.exists()).scalar():
                    room_number=int(input("\nwhat is the room number?"))
                    q = sess.query(rooms.number).filter(rooms.number == room_number)
                door_name=""
                q = sess.query(door_formats.name).filter(door_formats.name == door_name)
                while not sess.query(q.exists()).scalar():
                    door_name=input("\nwhat is the door name?")
                    q = sess.query(door_formats.name).filter(door_formats.name == door_name)
                room: rooms=rooms(room_number, building_name)
                door: doors=doors(room, door_name)
                sess.add(door)
                sess.commit()
                print("door created in "+f'{building_name}'+" "+f'{room_number}')

            elif option=="i":
                print("Update access request to move to new employee")
                rr = -1
                #check valid id
                q = sess.query(room_requests.request_id).filter(room_requests.request_id==rr)
                while not sess.query(q.exists()).scalar():
                    rr = int(input("\n\n\nEnter valid request ID to move to different employee: "))
                    q = sess.query(room_requests.request_id).filter(room_requests.request_id == rr)
                prev_empid=sess.query(room_requests.employee_id).filter(room_requests.request_id==rr)
                empid=-1
                q = sess.query(employees.id).filter(employees.id==empid)
                while not sess.query(q.exists()).scalar():
                    empid = int(input("\n\n\nEnter valid employee ID to move request to: "))
                    q = sess.query(employees.id).filter(employees.id == empid)
                updt = sess.update(room_requests).where(room_requests.request_id==rr).values(request_date=datetime.now(), employee_id=empid)
                engine.execute(updt)
                print("\nRequest "+f'{rr}'+"updated from employee "+f'{prev_empid}'+" to employee "+f'{empid}')

            elif option=="j":
                print("Report all employees who can get into a room")
                b_name = ""
                #check valid building
                q = sess.query(building.name).filter(building.name==b_name)
                while not sess.query(q.exists()).scalar():
                    b_name=(input("\n\n\nValid building name you want access to: ")).upper()
                    q = sess.query(building.name).filter(building.name == b_name)
                r_num = -1
                q = sess.query(rooms.number).filter(rooms.number==r_num)
                while not sess.query(q.exists()).scalar():
                    r_num = int(input("Enter valid room number: "))
                    q = sess.query(rooms.number).filter(rooms.number == r_num)
                #get requent id numbers for room
                request = sess.query(room_requests.request_id).filter(room_requests.room_number==r_num,
                                                                      room_requests.building_name==b_name).all()
                request = [request_id for request_id, in request]
                result = sess.query(key_issues.request_id).filter(key_issues.request_id.in_(request)).all()
                req_res = [request_id for request_id, in result]
                response = sess.query(room_requests.employee_id).filter(room_requests.request_id.in_(req_res)).all()
                print("\nEmployees that can enter "+f'{b_name}'+" "+f'{r_num}'+" are employees: "+f'{response}')
            elif option=="q":
                print("goodbye")
            else:
                print('Choose another option')