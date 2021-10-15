import requests
from typing import Dict, List
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .db import *
from drf_yasg.utils import swagger_auto_schema
from .decorators import db_init_with_credentials

from apscheduler.schedulers.background import BackgroundScheduler

EVENTS: Dict[str, str] = {"enter": "enter_organization", "leave": "leave_organization"}


@api_view(["GET", "POST"])
def sync_notifier(request):
    try:
        # scheduler = BackgroundScheduler()
        # scheduler.start()
        return Response({"status": True, "message": "OK"}, status=status.HTTP_200_OK)
    except:
        return Response(
            {
                "status": False,
            },
            status.HTTP_400_BAD_REQUEST,
        )

    return Response(data=request.data, status=status.HTTP_200_OK)


def job():
    # Retrieve the queue for synchronization
    queue = getQueue()
    if not queue:
        return Response(data="No data to update", status=status.HTTP_404_NOT_FOUND)

    # Process if new data to update
    last_queue_id = queue[len(queue) - 1]("id")

    for data in queue:
        if data["event"] == EVENTS.get("enter"):
            pass

        if data["event"] == EVENTS.get("leave"):
            pass
    return Response(data="ok", status=status.HTTP_200_OK)
