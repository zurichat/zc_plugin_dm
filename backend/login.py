import requests

def login_user():
    data = {
    "email":"sam@gmail.com",
    "password": "Owhondah"

    }
    try:
        response = requests.post(url="https://api.zuri.chat/auth/login", json=data)
    except requests.exceptions.RequestException as e:
        return None
    return response.json()["data"]["user"]["token"]
