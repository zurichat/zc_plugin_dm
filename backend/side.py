from db import DB
import requests
import json

response = DB.read("dm_rooms")
print(response)

user=1987
org=1
# url=f"https://channels.zuri.chat/api/v1/sidebar/?org={org}&user={user}"
# response=requests.get(url)
# print(response.text)
