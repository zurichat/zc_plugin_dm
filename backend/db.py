import re
from urllib.parse import urlencode
from django.http import response
import requests, json
from datetime import datetime, timedelta


from requests import exceptions


def login_user():
    data = {"email": "sam@gmail.com", "password": "Owhondah"}
    try:
        response = requests.post(url="https://api.zuri.chat/auth/login", json=data)
    except requests.exceptions.RequestException as e:
        return e
    if response.status_code == 200:
        return response.json()["data"]["user"]["token"]
    else:
        return None


PLUGIN_ID = "61696380b2cc8a9af4833d80"
ORG_ID = "61695d8bb2cc8a9af4833d46"
CENTRIFUGO_TOKEN = "58c2400b-831d-411d-8fe8-31b6e337738b"
ROOMS = "dm_rooms"
MESSAGES = "dm_messages"
header = {"Authorization": f"Bearer {login_user()}"}


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
        self.delete_file_api = "https://api.zuri.chat/delete/file/{pgn_id}"
        self.read_query_api = "https://api.zuri.chat/data/read"

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

    def read_query(
        self,
        collection_name: str,
        resource_id: str = None,
        query: dict = {},
        options: dict = {},
    ):
        request_body = {
            "collection_name": collection_name,
            "filter": query,
            "object_id": resource_id,
            "organization_id": self.organization_id,
            "plugin_id": self.plugin_id,
            "options": options,
        }

        try:
            response = requests.post(url=self.read_query_api, json=request_body)
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

    def upload(self, file, token):  # takes in files oh, 1 file
        url = self.upload_multiple_api.format(pgn_id=self.plugin_id)
        files = {"file": file}
        try:
            response = requests.post(
                url=url, files=files, headers={"Authorization": f"{token}"}
            )
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": response.status_code, "message": response.reason}

    def upload_more(self, files, token):
        url = self.upload_multiple_api.format(pgn_id=self.plugin_id)
        try:
            response = requests.post(
                url=url, files=files, headers={"Authorization": f"{token}"}
            )
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": response.status_code, "message": response.reason}

    def delete_file(self, file_url):
        url = self.delete_file_api.format(pgn_id=self.plugin_id)

        body = dict(file_url=file_url)

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
    query = {"room_user_ids":user_id}
    options = {"sort":{"created_at":-1}}
    response = helper.read_query("dm_rooms", query=query, options=options)

    if response and "status_code" not in response:
        return response
    return []


# get all the messages in a particular room
def get_room_messages(room_id, org_id):
    helper = DataStorage()
    helper.organization_id = org_id
    options = {"sort":{"created_at":-1}}
    response = helper.read_query("dm_messages", query={"room_id": room_id}, options=options)
    if response and "status_code" not in response:
        return response
    return []


# get all the messages in a particular room filtered by date
def get_messages(room_id,org_id, date):
    helper = DataStorage()
    helper.organization_id = org_id
    req_date = datetime.strptime(date, '%d-%m-%Y')
    next_day = req_date + timedelta(days=1)
    options = {"sort":{"created_at":-1}}
    query = {
        "$and":[
        {"room_id":room_id},
        {"created_at":{
            "$gte":str(req_date),
            "$lt": str(next_day)
        }}
        ]
    }
    
    response = helper.read_query("dm_messages", query=query, options=options)
    if response and "status_code" not in response:
        return response
    return []
    


def get_user_profile(org_id=None, user_id=None):
    profile = requests.get(
        f"https://api.zuri.chat/organizations/{org_id}/members/{user_id}",
        headers=header,
    )
    return profile.json()


def get_all_organization_members(org_id: str):
    response = requests.get(
        f"https://api.zuri.chat/organizations/{org_id}/members/"
    )
    if response.status_code == 200:
        return response.json()["data"]
    return None


def get_member(members: list, member_id: str):
    for member in members:
        if member["_id"] == member_id:
            return member
    return {}


def sidebar_emitter(
    org_id, member_id, group_room_name=None
):  # group_room_name = None or a String of Names
    rooms = []
    starred_rooms = []
    user_rooms = get_rooms(user_id=member_id, org_id=org_id)
    members = get_all_organization_members(org_id)
    
    if user_rooms != None:
        for room in user_rooms:
            room_profile = {}
            if len(room['room_user_ids']) == 2:
                room_profile["room_id"] = room["_id"]
                room_profile["room_url"] = f"/dm/{room['_id']}"
                user_id_set = set(room['room_user_ids']).difference({member_id})
                partner_id = list(user_id_set)[0]              
                
                profile = get_member(members,partner_id)

                if "user_name" in profile and profile['user_name'] != "":
                    if profile["user_name"]:
                        room_profile["room_name"] = profile["user_name"]
                    else:
                        room_profile["room_name"] = "no user name"
                    if profile["image_url"]:
                        room_profile["room_image"] = profile["image_url"]
                    else:
                        room_profile[
                            "room_image"
                        ] = "https://cdn.iconscout.com/icon/free/png-256/account-avatar-profile-human-man-user-30448.png"
                    
                else:
                    room_profile["room_name"] = "no user name"
                    room_profile[
                        "room_image"
                    ] = "https://cdn.iconscout.com/icon/free/png-256/account-avatar-profile-human-man-user-30448.png"
            else:
                room_profile["room_name"] = room["room_name"]
                room_profile["room_id"] = room["_id"]
                room_profile["room_url"] = f"/dm/{room['_id']}"

            rooms.append(room_profile)

            if member_id in room["starred"]:
                starred_rooms.append(room_profile)
                
    side_bar = {
        "event":"sidebar_update",
        "plugin_id":"dm.zuri.chat",
        "data":{
        "name": "DM Plugin",
        "description": "Sends messages between users",
        "plugin_id": "dm.zuri.chat",
        "organisation_id": f"{org_id}",
        "user_id": f"{member_id}",
        "group_name": "DM",
        "category": "direct messages",
        "show_group": False,
        "button_url": f"/dm",
        "public_rooms": [],
        "starred_rooms": starred_rooms,
        "joined_rooms": rooms,
        }
        # List of rooms/collections created whenever a user starts a DM chat with another user
        # This is what will be displayed by Zuri Main
    }
    return side_bar


# gets starred rooms
def get_starred_rooms(member_id, org_id):
    """goes through database and returns starred rooms"""
    response = get_rooms(member_id, org_id)
    if response:
        data = []
        for room in response:
            try:
                star = room["starred"]
                if member_id in star:
                    data.append(room)
            except Exception:
                pass
        return data
    else:
        if response == [] or isinstance(response, dict):
            return []


def getQueue():
    """Get queue data from the plugin information

    Returns:
        [type]: [description]
    """
    dm_plugin_url = f"https://api.zuri.chat/marketplace/plugins/{PLUGIN_ID}"
    try:
        response = requests.get(url=dm_plugin_url)
    except requests.exceptions.RequestException as e:
        return e
    if response.status_code == 200:
        return response.json()["data"]["queue"]
    else:
        return None


def update_queue_sync(queue_id: int):
    """Patch with the last queue id

    Args:
        queue_id (int): The last queue id that has been updated

    Returns:
        [type]: [description]
    """
    patch_queue_url = f"https://api.zuri.chat/plugins/{PLUGIN_ID}/sync"
    body = {"id": queue_id}
    try:
        response = requests.patch(url=patch_queue_url, json=body)
    except requests.exceptions.RequestException as e:
        return e
    if response.status_code == 200:
        return response.json()
    else:
        return None


