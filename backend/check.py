from db import *

db = DataStorage()

rooms = db.read("dm_rooms")

collection = "dm_rooms"
org_id ="6133c5a68006324323416896"
user = "lkdl049052098509292"

my_room = get_rooms(user)

#print(my_room)
#print(rooms)

a = ["asdf;lkj", "12340987"]
b = ["12340987", "asdf;lkj"]
c = ["12340987", "zxcv.,mn"]
d = ["werqwtte", "[poippoi"]
test_id = ['lkdl049052098509292', 'al09952090529302']

user_ids = ['lkdl049052098509292', 'al09952090529302']
user_rooms = get_rooms(user_ids[0]) + get_rooms(user_ids[1])
for room in user_rooms:
    ids = room['room_user_ids']
    if set(ids)==set(test_id):
        room_id = {"room_id":room["_id"]}
        print(room_id)

    else:
        print("not found")
        break


test_json = {
    "org_id": "aoiueoi9e8r8q9e33q4rwofi",
    "room_user_ids": ['lkdl049052098509292', 'al09952090529302'],
    "bookmarks": [],
    "pinned":[]
}