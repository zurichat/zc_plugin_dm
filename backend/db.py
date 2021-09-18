from urllib.parse import urlencode
import requests, json


PLUGIN_ID = "6135f65de2358b02686503a7"
ORG_ID = "6133c5a68006324323416896"
CENTRIFUGO_TOKEN = "58c2400b-831d-411d-8fe8-31b6e337738b"


class DataStorage:
    def __init__(self, request=None):
        self.read_api = (
            "https://api.zuri.chat/data/read/{pgn_id}/{collec_name}/{org_id}?{query}"
        )
        self.write_api = "https://api.zuri.chat/data/write"
        self.delete_api = "https://api.zuri.chat/data/delete"

        if request is None:
            self.plugin_id = PLUGIN_ID
            self.organization_id = ORG_ID
        else:
            self.plugin_id = request.data.get("plugin_id")
            self.organization_id = request.data.get("org_id")

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


def send_centrifugo_data(room, data):
    url = "https://realtime.zuri.chat/api"
    # url = "http://localhost:8000/api"
    headers = {
        "Content-type": "application/json",
        "Authorization": "apikey " + CENTRIFUGO_TOKEN,
    }
    command = {"method": "publish", "params": {"channel": room, "data": data}}
    try:
        response = requests.post(url=url, headers=headers, json=command)
        return {"status_code": response.status_code, "message": response.json()}
    except Exception as e:
        print(e)


DB = DataStorage()


def get_user_rooms(collection_name, org_id, user):
    room_list = list()
    rooms = DB.read(collection_name, {"org_id": org_id})
    if rooms == None or "status_code" in rooms:
        return rooms
    else:
        for room in rooms:
            if "room_user_ids" in room:
                if user in room.get("room_user_ids"):
                    room_list.append(room)
                else:
                    return room_list
        return room_list


# get rooms for a particular user
def get_rooms(user_id):
    """Get the rooms a user is in

    Args:
        user_id (str): The user id

    Returns:
        [List]: [description]
    """    
    response = DB.read("dm_rooms")
    data =  []
    if response != None:
        if "status_code" in response:
            return response
        for room in response:
            try:
                users_room_list = room['room_user_ids']
                if user_id in users_room_list:
                    data.append(room)
            except Exception:
                pass
        if len(data) == 0:
            data = None
            return data
        return data
    
    return response


# get all the messages in a particular room
def get_room_messages(room_id):
    response = DB.read("dm_messages", {'room_id': room_id})
    if response != None:
        if "status_code" in response:
            return response
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