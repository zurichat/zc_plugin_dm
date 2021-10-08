import re
from urllib.parse import urlencode
from django.http import response
import requests, json


def login_user():
    data = {
        "email": "sam@gmail.com",
        "password": "Owhondah"
    }
    try:
        response = requests.post(url="https://api.zuri.chat/auth/login", json=data)
    except requests.exceptions.RequestException as e:
        return e
    if response.status_code==200:
        return response.json()["data"]["user"]["token"]
    else:
        return None

PLUGIN_ID = "6135f65de2358b02686503a7"
ORG_ID = "614679ee1a5607b13c00bcb7"
CENTRIFUGO_TOKEN = "58c2400b-831d-411d-8fe8-31b6e337738b"
ROOMS = "dm_rooms"
MESSAGES = "dm_messages"
header={
    'Authorization': f'Bearer {login_user()}'
}
class DataStorage:
    def __init__(self, request=None):
        self.read_api = (
            "https://api.zuri.chat/data/read/{pgn_id}/{collec_name}/{org_id}?{query}"
        )
        # self.upload_test_api = "http://127.0.0.1:8000/api/v1/testapi/{pgn_id}"
        self.write_api = "https://api.zuri.chat/data/write"
        self.delete_api = "https://api.zuri.chat/data/delete"
        self.upload_api = "https://api.zuri.chat/upload/file/{pgn_id}"
        self.upload_multiple_api = "https://api.zuri.chat/upload/files/{pgn_id}"
        self.delete_file_api ="https://api.zuri.chat/delete/file/{pgn_id}"

        if request is None:
            self.plugin_id = PLUGIN_ID
            self.organization_id = ORG_ID
        else:
            self.plugin_id = request.META.get("PLUGIN_ID", PLUGIN_ID)
            self.organization_id = request.META.get("ORG_ID")

    def write(self, collection_name, data):
        body = dict(
            plugin_id=self.plugin_id,
            organization_id=self.organization_id,
            collection_name=collection_name,
            payload=data,
        )
        try:
            response = requests.post(url=self.write_api, json=body)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 201:
            return response.json()
        else:
            return {"status_code": response.status_code, "message": response.reason}

    def update(self, collection_name, document_id, data):
        body = dict(
            plugin_id=self.plugin_id,
            organization_id=self.organization_id,
            collection_name=collection_name,
            object_id=document_id,
            payload=data,
        )
        try:
            response = requests.put(url=self.write_api, json=body)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return {"status_code": response.status_code, "message": response.reason}

    def read(self, collection_name, filter={}):
        try:
            query = urlencode(filter)
        except Exception as e:
            print(e)
            return None

        url = self.read_api.format(
            pgn_id=self.plugin_id,
            org_id=self.organization_id,
            collec_name=collection_name,
            query=query,
        )

        try:
            response = requests.get(url=url)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json().get("data")
        else:
            return {"status_code": response.status_code, "message": response.reason}

    def delete(self, collection_name, document_id):
        body = dict(
            plugin_id=self.plugin_id,
            organization_id=self.organization_id,
            collection_name=collection_name,
            object_id=document_id,
        )
        try:
            response = requests.post(url=self.delete_api, json=body)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return {"status_code": response.status_code, "message": response.reason}

    def upload(self, file, token):                   #takes in files oh, 1 file
        url = self.upload_multiple_api.format(
            pgn_id = self.plugin_id
        )
        files = {"file":file}
        try:
            response = requests.post(url=url, files=files, headers={
                'Authorization': f'{token}'
                })
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": response.status_code, "message": response.reason}

    def upload_more(self, files, token):
        url = self.upload_multiple_api.format(
            pgn_id = self.plugin_id
        )
        print(files)  #Just testing shii
        try:
            response = requests.post(url=url, files=files, headers={
                'Authorization': f'{token}'
                })
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": response.status_code, "message": response.reason}

    def delete_file(self, file_url):
        url = self.delete_file_api.format(
            pgn_id = self.plugin_id
        )

        body = dict(
            file_url=file_url
        )

        try:
            response = requests.post(url=url, json=body)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return {"status_code": response.status_code, "message": response.reason}







DB = DataStorage()


# get rooms for a particular user
def get_rooms(user_id, org_id):
    """Get the rooms a user is in

    Args:
        user_id (str): The user id

    Returns:
        [List]: [description]
    """

    helper = DataStorage()
    helper.organization_id = org_id
    response = helper.read("dm_rooms")
    data =  []
    if response != None:
        if "status_code" in response:
            return None
        for room in response:
            if "room_user_ids" in room:
                try:
                    users_room_list = room["room_user_ids"]
                    if user_id in users_room_list:
                        data.append(room)
                except Exception:
                    pass
        if len(data) == 0:
            data = []
            return data
        return data
    return None


# get all the messages in a particular room
def get_room_messages(room_id, org_id):
    helper = DataStorage()
    helper.organization_id = org_id
    response = helper.read("dm_messages", {'room_id': room_id})
    if response != None:
        if "status_code" in response:
            return response
        if len(response) == 0:
            response = None
            return response
        for message in response:
            message["id"] = message.pop("_id")
        response.reverse()
        return response
    return response



# get all the messages in a particular room filtered by date
def get_messages(response, date):
    res = []
    if response != None:
        if "status_code" in response:
            return response
        for message in response:
            try:
                query_date = message['created_at'].split("T")[0]
                if query_date == date:
                    res.append(message)
            except Exception:
                pass
        if len(res) == 0:
            res = None
            return res
        return res
    return response


def get_user_profile(org_id=None, user_id=None):
    profile = requests.get(f"https://api.zuri.chat/organizations/{org_id}/members/{user_id}", headers=header)
    return profile.json()


def sidebar_emitter(org_id, member_id, group_room_name=None):  # group_room_name = None or a String of Names
    user_rooms = get_rooms(user_id=member_id, org_id=org_id)
    rooms = []
    if user_rooms == None:
        pass
    else:
        for room in user_rooms:
            if org_id == room["org_id"]:
                room_profile = {}
                for user_id in room["room_user_ids"]:
                    if user_id != member_id:
                        print (user_id)
                        profile = get_user_profile(org_id, user_id)
                        if profile["status"] == 200:
                            
                            
                            if group_room_name and len(group_room_name.split(',')) > 2:  # if group_room_name != None && Len of List after split > 2
                                room_profile["room_name"] = group_room_name  # overwrite room_name in profile to = String of Names
                            else:
                                room_profile["room_name"] = profile["data"]["user_name"]
                                
                            
                            if profile["data"]["image_url"]:
                                room_profile["room_image"] = profile["data"]["image_url"]
                            else:
                                room_profile[
                                    "room_image"
                                ] = "https://cdn.iconscout.com/icon/free/png-256/account-avatar-profile-human-man-user-30448.png"
                            rooms.append(room_profile)
                    room_profile["room_url"] = f"/dm/{org_id}/{room['_id']}/{member_id}"
    if len(rooms) > 1:
        return rooms[-1]
    else:
        return rooms