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

    hook = db.hooks
    hook.delete_many({})
    my_hook = hook.insert_many([
        {"hook_id": 12345}
    ])

    key = db.keys
    key.delete_many({})
    my_key = key.insert_many([
        {"serial_number":123456,
        "hook_id":DBRef("hook_id",db.hooks.find_one({"hook_id":12345})['_id'])}
    ])

    employee = db.employees
    employee.delete_many({})
    my_employee = employee.insert_many([
        {"employee_id":1234567, "name":"David Brown", "fine":0.00}
    ])

    room = db.rooms
    room.delete_many({})
    my_room = room.insert_many([
        {"number":308,"building_name":DBRef("building",db.building.find_one({"name":"ECS"})['_id'])}
    ])

    rr = db.room_requests
    rr.delete_many({})
    my_rr = rr.insert_many([
        {"request_date":str(date.today()),
         "employee_id":DBRef("employees",db.employees.find_one({"employee_id":1234567})['_id']),
         "room_number":DBRef("rooms",db.rooms.find_one({"number":308})['_id']),
         "building_name":DBRef("building",db.building.find_one({"name":"ECS"})['_id'])}
    ])

    ki = db.key_issues
    ki.delete_many({})
    my_ki = ki.insert_many([
        {"issue_time":datetime.now().strftime("%H:%M:%S"),
         "issue_date":str(date.today()),
         "key_number":DBRef("keys",db.keys.find_one({"serial_number":123456})['_id']),
         "request_date":DBRef("room_requests",db.room_requests.find_one({"request_date":str(date.today())})['_id']),
         "employee_id": DBRef("employees", db.employees.find_one({"employee_id": 1234567})['_id']),
         "room_number": DBRef("rooms", db.rooms.find_one({"number": 308})['_id']),
         "building_name": DBRef("building", db.building.find_one({"name": "ECS"})['_id'])}
    ])

    lk = db.lost_keys
    lk.delete_many({})
    my_lk = lk.insert_many([
        {"lost_time":datetime.now().strftime("%H:%M:%S"),
         "lost_date": str(date.today()),
         "request_date": DBRef("room_requests", db.room_requests.find_one({"request_date": str(date.today())})['_id']),
         "employee_id": DBRef("employees", db.employees.find_one({"employee_id": 1234567})['_id']),
         "room_number": DBRef("rooms", db.rooms.find_one({"number": 308})['_id']),
         "building_name": DBRef("building", db.building.find_one({"name": "ECS"})['_id'])}
    ])

