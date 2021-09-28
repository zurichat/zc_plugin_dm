from datetime import datetime
from datetime import timezone
from threading import Thread
import time
from .db import send_centrifugo_data
 
class SendNotificationThread(Thread):
    # def __init__(self, duration, room_id, response_output,scheduled_date):
    def __init__(self, duration, duration_sec, utc_scheduled_date, utc_current_date):
    
        self.duration = duration
        self.duration_sec = duration_sec
        self.utc_scheduled_date = utc_scheduled_date
        self.utc_current_date = utc_current_date
        Thread.__init__(self)

    def run(self):
        while True:
            print(self.utc_scheduled_date)
            time.sleep(self.duration_sec)
            current_date = self.utc_current_date + self.duration
            #notification sent to user
            # centrifugo_data = send_centrifugo_data(room=room_id, data=response_output)  # publish data to centrifugo
            if self.utc_scheduled_date == current_date:
                print('notification sent')
                break
        
        # for conn in connections:
        #     conn.close()

# create new thread to call api

# On a separate note, if you are using uWSGI in deployment, you need to add

# --enable-threads
# argument to enable multi threading.