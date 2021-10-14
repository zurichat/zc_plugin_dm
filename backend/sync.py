import requests
from typing import Dict, List
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .db import *
from drf_yasg.utils import swagger_auto_schema
from .decorators import db_init_with_credentials


async def sync_notifier():
    print("json")
