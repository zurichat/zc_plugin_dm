from datetime import datetime
from datetime import timezone
from threading import Thread
import time
from .db import send_centrifugo_data
 
class SendNotificationThread(Thread):
    def __init__(self, duration, room_id, response_output,scheduled_date):
        self.duration = duration
        self.room_id = room_id
        self.response_output = response_output
        self.scheduled_date = scheduled_date.replace(tzinfo=timezone.utc, microsecond=0)
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(self.duration)
            current_time = datetime.now(timezone.utc)

            #notification sent to user
            centrifugo_data = send_centrifugo_data(room=room_id, data=response_output)  # publish data to centrifugo
            if self.scheduled_date == current_time:
                break
        
        for conn in connections:
            conn.close()

# create new thread to call api

# On a separate note, if you are using uWSGI in deployment, you need to add

# --enable-threads
# argument to enable multi threading.