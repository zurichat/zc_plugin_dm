import requests


def login_user():
    data = {
        "email": "sam@gmail.com",
        "password": "Owhondah"
    }
    try:
        response = requests.post(url="https://api.zuri.chat/auth/login", json=data)
    except requests.exceptions.RequestException as e:
        return None
    if response.status_code==200:
        return response.json()["data"]["user"]["token"]
    else:
        return None
