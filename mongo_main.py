import time

import pymongo
from pymongo import MongoClient
from bson import DBRef

from datetime import *

if __name__=='__main__':
    cluster = 'mongodb+srv://Tony:NeoGeoFanbase#1@cluster0.jts7qvr.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(cluster)
    db = client.key_hook
    print("In main:", db.list_collection_names())

    building = db.building
    building.delete_many({})
    my_building = building.insert_many([
        {"name":"ECS"}
    ])
    building_validator = {
        'validator': {
            '$jsonSchema': {
                # Signifies that this schema is complex, has parameters within it.
                # These can be nested.
                'bsonType': "object",
                'description': "Valid building name",
                'required': ["name"],
                'additionalProperties': False,
                'properties': {
                    # I would LIKE to demand an ObjectID here, but I cannot figure out how
                    '_id': {},
                    'name': {
                        'bsonType': "string",
                        "description": "building name"
                    }
                }
            }
        }
    }
    db.command('collMod', 'building', **building_validator)

    hook = db.hooks
    hook.delete_many({})
    my_hook = hook.insert_many([
        {"hook_id": 12345}
    ])
    hook_validator = {
        'validator': {
            '$jsonSchema': {
                # Signifies that this schema is complex, has parameters within it.
                # These can be nested.
                'bsonType': "object",
                'description': "Valid hook id",
                'required': ["hook_id"],
                'additionalProperties': False,
                'properties': {
                    # I would LIKE to demand an ObjectID here, but I cannot figure out how
                    '_id': {},
                    'name': {
                        'bsonType': "int",
                        "description": "hook id"
                    }
                }
            }
        }
    }
    db.command('collMod', 'hook', **hook_validator)

    # key = db.keys
    # key.delete_many({})
    # my_key = key.insert_many([
    #     {"serial_number":123456,
    #     "hook_id":DBRef("hook_id",db.hooks.find_one({"hook_id":12345})['_id'])}
    # ])

    # employee = db.employees
    # employee.delete_many({})
    # my_employee = employee.insert_many([
    #     {"employee_id":1234567, "name":"David Brown", "fine":0.00}
    # ])

    # room = db.rooms
    # room.delete_many({})
    # my_room = room.insert_many([
    #     {"number":308,"building_name":DBRef("building",db.building.find_one({"name":"ECS"})['_id'])}
    # ])

    # rr = db.room_requests
    # rr.delete_many({})
    # my_rr = rr.insert_many([
    #     {"request_date":str(date.today()),
    #      "employee_id":DBRef("employees",db.employees.find_one({"employee_id":1234567})['_id']),
    #      "room_number":DBRef("rooms",db.rooms.find_one({"number":308})['_id']),
    #      "building_name":DBRef("building",db.building.find_one({"name":"ECS"})['_id'])}
    # ])

    # ki = db.key_issues
    # ki.delete_many({})
    # my_ki = ki.insert_many([
    #     {"issue_time":datetime.now().strftime("%H:%M:%S"),
    #      "issue_date":str(date.today()),
    #      "key_number":DBRef("keys",db.keys.find_one({"serial_number":123456})['_id']),
    #      "request_date":DBRef("room_requests",db.room_requests.find_one({"request_date":str(date.today())})['_id']),
    #      "employee_id": DBRef("employees", db.employees.find_one({"employee_id": 1234567})['_id']),
    #      "room_number": DBRef("rooms", db.rooms.find_one({"number": 308})['_id']),
    #      "building_name": DBRef("building", db.building.find_one({"name": "ECS"})['_id'])}
    # ])

    # lk = db.lost_keys
    # lk.delete_many({})
    # my_lk = lk.insert_many([
    #     {"lost_time":datetime.now().strftime("%H:%M:%S"),
    #      "lost_date": str(date.today()),
    #      "request_date": DBRef("room_requests", db.room_requests.find_one({"request_date": str(date.today())})['_id']),
    #      "employee_id": DBRef("employees", db.employees.find_one({"employee_id": 1234567})['_id']),
    #      "room_number": DBRef("rooms", db.rooms.find_one({"number": 308})['_id']),
    #      "building_name": DBRef("building", db.building.find_one({"name": "ECS"})['_id'])}
    # ])

    option = ""
    while option != "q":
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

        op = op.lower()
        if option == 'a':
            print("Creating a key")
            hook = 0
        #     q = sess.query(hooks.hook_id).filter(hooks.hook_id == hook)
        
        #     while not sess.query(q.exists()).scalar():
        #         hook = int(input("\n\n\nValid hook ID to make a copy of: "))
        #         q = sess.query(hooks.hook_id).filter(hooks.hook_id == hook)
        #     newKey: keys = keys(hook_id=hook)
        #     sess.add(newKey)
        #     sess.commit()
        #     print("\n\nNew Key(" + f'{newKey.serial_number}' + ") created")
        #
        # elif option == 'b':
        #     print("Request access to room")
        #     empid = 0
        #     # check valid id
        #     q = sess.query(employees.id).filter(employees.id == empid)
        #     while not sess.query(q.exists()).scalar():
        #         empid = input("\n\n\nEnter valid employee ID: ")
        #         q = sess.query(employees.id).filter(employees.id == empid)
        #     bn = ""
        #     # check valid building
        #     q = sess.query(building.name).filter(building.name == bn)
        #     while not sess.query(q.exists()).scalar():
        #         bn = (input("\n\n\nValid building you want to access: ")).upper()
        #         q = sess.query(building.name).filter(building.name == bn)
        #     rn = -1
        #     # check valid room number
        #     q = sess.query(rooms.number).filter(rooms.number == rn)
        #     while not sess.query(q.exists()).scalar():
        #         rn = input("\n\n\nRoom number you want to access: ")
        #         q = sess.query(rooms.number).filter(rooms.number == rn)
        #     room: rooms = rooms(num=rn, bn=bn)
        #     print("\nCreating room request...\n")
        #     request: room_requests = room_requests(id=empid, room=room)
        #     sess.add(request)
        #     sess.commit()
        #
        # elif option == "c":
        #     print("Issue key to an employee")
        #     rr = -1
        #     # check valid id
        #     q = sess.query(room_requests.request_id).filter(room_requests.request_id == rr)
        #     while not sess.query(q.exists()).scalar():
        #         rr = int(input("\n\n\nEnter valid request ID: "))
        #         q = sess.query(room_requests.request_id).filter(room_requests.request_id == rr)
        #     request = sess.query(room_requests).filter(room_requests.request_id == rr).scalar()
        #     door = sess.query(doors).filter(doors.building_name == request.building_name,
        #                                     doors.room_number == request.room_number).scalar()
        #     acc = sess.query(access).filter(access.door_id == door.door_id).scalar()
        #     key = sess.query(keys).filter(room_requests.room_number == door.room_number,
        #                                   room_requests.building_name == door.building_name,
        #                                   keys.hook_id == acc.hook_id).scalar()
        #     print("\nIssuing key...\n")
        #     issue: key_issues = key_issues(rid=request, eid=request.employee_id, key=key)
        #     sess.add(issue)
        #     sess.commit()
        #     print("\nKey (" + f'{key.key_number}' + ") issued to employee ID: " + f'{issue.employee_id}'
        #           + "at " + f'{issue.request_date}' + "\n")
        #
        # elif option == "d":
        #     print("\n\n\nReport lost key")
        #     empid = -1
        #     # check valid id
        #     q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
        #     while not sess.query(q.exists()).scalar():
        #         empid = int(input("\n\n\nEnter valid ID issued: "))
        #         q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
        #     keyid = -1
        #     q = sess.query(key_issues.key_number).filter(key_issues.key_number == keyid)
        #     while not sess.query(q.exists()).scalar():
        #         keyd = int(input("\n\n\nEnter valid key ID issued to employee: "))
        #         q = sess.query(key_issues.key_number).filter(key_issues.key_number == keyid)
        #     print("\nReporting key as lost...\n")
        #     lost: lost_key = lost_key()
        #     sess.add(lost)
        #     sess.commit()
        #     print("\nKey " + f'{keyid}' + " Reported lost at: " + f'{lost.request_date}'), print()
        #     updt = sess.update(employees).where(employees.id == empid).values(fine=employees.fine + 25)
        #     engine.execute(updt)
        #     print(f'{empid}' + " was fined $25")
        #
        # elif option == "e":
        #     print("Report out all the rooms an employee can enter given the keys they already have")
        #     empid = -1
        #     q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
        #     while not sess.query(q.exists()).scalar():
        #         empid = int(input("\n\n\nEnter valid employee ID: "))
        #         q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
        #     request_list = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid).all()
        #     request_list = [employee_id for employee_id, in request_list]
        #     result = sess.query(room_requests.room_number).filter(room_requests.request_id.in_(request_list)).all()
        #     print("\nEmployee " + f'{empid}' + " has access to rooms: " + f'{result}')
        #
        # elif option == "f":
        #     print("Delete a key")
        #     kid = int(input("\n\n\nEnter valid key ID to delete: "))
        #     try:
        #         delete_lost = sess.query(lost_key).filter(lost_key.key_number == kid).all()
        #         for obj in delete_lost:
        #             sess.delete(obj)
        #     except:
        #         print("No key was found")
        #     try:
        #         delete_issued = sess.query(key_issues).filter(key_issues.key_number == kid).all()
        #     except:
        #         print("No key was found")
        #     delete_user = sess.query(keys).filter(keys.serial_number == kid).all()
        #     for obj in delete_user:
        #         sess.delete(obj)
        #     sess.commit()
        #     print("\nKey deleted")
        #
        # elif option == "g":
        #     print("Delete an employee")
        #     empid = -1
        #     q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
        #     while not sess.query(q.exists()).scalar():
        #         empid = int(input("\n\n\nEnter valid employee ID: "))
        #         q = sess.query(key_issues.employee_id).filter(key_issues.employee_id == empid)
        #     # delete employee in lost key
        #     d_emp_lost = sess.query(lost_key).filter(lost_key.employee_id == empid).all()
        #     for obj in d_emp_lost:
        #         sess.delete(obj)
        #         print("Deleted employee in lost key")
        #     # delete employee in issued key
        #     d_emp_iss = sess.query(key_issues).filter(key_issues.employee_id == empid).all()
        #     for obj in d_emp_iss:
        #         sess.delete(obj)
        #         print("Deleted employee in issued key")
        #     # delete employee in room request
        #     d_emp_rr = sess.query(room_requests).filter(room_requests.employee_id == empid).all()
        #     for obj in d_emp_rr:
        #         sess.delete(obj)
        #         print("Deleted employee in room request")
        #     # delete employee in employee
        #     d_emp = sess.query(employees).filter(employees.id == empid).all()
        #     for obj in d_emp:
        #         sess.delete(obj)
        #         print("Deleted employee")
        #     sess.commit()
        #
        # elif option == "h":
        #     print("add a new door that can be opened by existing hook")
        #     building_name = ""
        #     # cehck valid building
        #     q = sess.query(building.name).filter(building.name == building_name)
        #     while not sess.query(q.exists()).scalar():
        #         building_name = input("\nWhat is the building name?").upper()
        #         q = sess.query(building.name).filter(building.name == building_name)
        #     room_number = -1
        #     q = sess.query(rooms.number).filter(rooms.number == room_number)
        #     while not sess.query(q.exists()).scalar():
        #         room_number = int(input("\nwhat is the room number?"))
        #         q = sess.query(rooms.number).filter(rooms.number == room_number)
        #     door_name = ""
        #     q = sess.query(door_formats.name).filter(door_formats.name == door_name)
        #     while not sess.query(q.exists()).scalar():
        #         door_name = input("\nwhat is the door name?")
        #         q = sess.query(door_formats.name).filter(door_formats.name == door_name)
        #     room: rooms = rooms(room_number, building_name)
        #     door: doors = doors(room, door_name)
        #     sess.add(door)
        #     sess.commit()
        #     print("door created in " + f'{building_name}' + " " + f'{room_number}')
        #
        # elif option == "i":
        #     print("Update access request to move to new employee")
        #     rr = -1
        #     # check valid id
        #     q = sess.query(room_requests.request_id).filter(room_requests.request_id == rr)
        #     while not sess.query(q.exists()).scalar():
        #         rr = int(input("\n\n\nEnter valid request ID to move to different employee: "))
        #         q = sess.query(room_requests.request_id).filter(room_requests.request_id == rr)
        #     prev_empid = sess.query(room_requests.employee_id).filter(room_requests.request_id == rr)
        #     empid = -1
        #     q = sess.query(employees.id).filter(employees.id == empid)
        #     while not sess.query(q.exists()).scalar():
        #         empid = int(input("\n\n\nEnter valid employee ID to move request to: "))
        #         q = sess.query(employees.id).filter(employees.id == empid)
        #     updt = sess.update(room_requests).where(room_requests.request_id == rr).values(request_date=date.today(),
        #                                                                                    employee_id=empid)
        #     engine.execute(updt)
        #     print("\nRequest " + f'{rr}' + "updated from employee " + f'{prev_empid}' + " to employee " + f'{empid}')
        #
        # elif option == "j":
        #     print("Report all employees who can get into a room")
        #     b_name = ""
        #     # check valid building
        #     q = sess.query(building.name).filter(building.name == b_name)
        #     while not sess.query(q.exists()).scalar():
        #         b_name = (input("\n\n\nValid building name you want access to: ")).upper()
        #         q = sess.query(building.name).filter(building.name == b_name)
        #     r_num = -1
        #     q = sess.query(rooms.number).filter(rooms.number == r_num)
        #     while not sess.query(q.exists()).scalar():
        #         r_num = int(input("Enter valid room number: "))
        #         q = sess.query(rooms.number).filter(rooms.number == r_num)
        #     # get requent id numbers for room
        #     request = sess.query(room_requests.request_id).filter(room_requests.room_number == r_num,
        #                                                           room_requests.building_name == b_name).all()
        #     request = [request_id for request_id, in request]
        #     result = sess.query(key_issues.request_id).filter(key_issues.request_id.in_(request)).all()
        #     req_res = [request_id for request_id, in result]
        #     response = sess.query(room_requests.employee_id).filter(room_requests.request_id.in_(req_res)).all()
        #     print("\nEmployees that can enter " + f'{b_name}' + " " + f'{r_num}' + " are employees: " + f'{response}')
        # elif option == "q":
        #     print("goodbye")
        # else:
        #     print('Choose another option')

