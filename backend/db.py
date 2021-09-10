
from urllib.parse import urlencode

import requests, json


PLUGIN_ID = "6135f65de2358b02686503a7"
ORG_ID = "6133c5a68006324323416896"
CENTRIFUGO_TOKEN = '58c2400b-831d-411d-8fe8-31b6e337738b'


class DataStorage:
    def __init__(self, request=None):
        self.read_api = "https://api.zuri.chat/data/read/{pgn_id}/{collec_name}/{org_id}?{query}"
        self.write_api = "https://api.zuri.chat/data/write"
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
            payload=data
        )
        try:
            response = requests.post(url=self.write_api, json=body)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 201:
            return response.json()
        else:
            return {
                "status_code": response.status_code,
                "message": response.reason
            }

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
            query=query
        )

        try:
            response = requests.get(url=url)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        if response.status_code == 200:
            return response.json().get("data")
        else:
            return {
                "status_code": response.status_code,
                "message": response.reason
            }


def send_centrifugo_data(room, data):
    url = "https://realtime.zuri.chat/api"
    headers = {'Content-type': 'application/json', 'Authorization': 'apikey ' + CENTRIFUGO_TOKEN}
    command = {
        "method": "publish",    
        "params": {
            "channel": room, 
            "data": data  
            }
        }
    try:
        response = requests.post(url=url,headers=headers, json=command)
        return {
                "status_code": response.status_code,
                "message": response.json()
            }
    except Exception as e:
        print(e)
        
    

DB = DataStorage()

# Gets the rooms that a user is in
def get_user_rooms(collection_name, org_id, user):
    room_list = list()
    rooms = DB.read(collection_name,{"org_id":org_id})
    if rooms==None or "status_code" in rooms:
        return rooms
    else:
        for room in rooms:
            if "room_user_ids" in room:
                if user in room["room_user_ids"]:
                    room_list.append(room)
                else:
                    return room_list
        return room_list
