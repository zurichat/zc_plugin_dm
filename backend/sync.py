from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .db import getQueue, update_queue_sync
from drf_yasg.utils import swagger_auto_schema
from .decorators import db_init_with_credentials

from apscheduler.schedulers.background import BackgroundScheduler

EVENTS = {"enter": "enter_organization", "leave": "leave_organization"}


@api_view(["GET", "POST"])
def sync_notifier(request) -> Response:
    """Receives a ping from zc_core about new data to synchronize.
    Then starts a background job to synchorize with the the new data in the queue

    Args:
        request (Request): The incoming request

    Returns:
        Response: The response returned
    """
    try:
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            job,
        )
        scheduler.start()
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
    """Process the queue for synchronization

    Returns:
        Response: The response returned
    """
    # Retrieve the queue for synchronization
    queue = getQueue()
    if not queue:
        return Response(data="No data to update", status=status.HTTP_404_NOT_FOUND)

    # Process if new data to update

    last_queue_id = queue[len(queue) - 1]["id"]

    for data in queue:
        org_id = data["message"]["organization_id"]
        member_id = data["message"]["member_id"]

        if data["event"] == "enter_organization":
            data = {
                "event": EVENTS.get("enter"),
                "org_id": org_id,
                "member_id": member_id,
            }

        if data["event"] == "leave_organization":
            data = {
                "event": EVENTS.get("leave"),
                "org_id": org_id,
                "member_id": member_id,
            }

    # sync with last queue id
    response = update_queue_sync(queue_id=last_queue_id)

    if response:
        return Response(data="Synchronized successfully", status=status.HTTP_200_OK)
    else:
        return Response(
            data="Synchronization failed", status=status.HTTP_424_FAILED_DEPENDENCY
        )
