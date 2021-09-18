from datetime import datetime
from threading import Thread
import time
 
class SendNotificationThread(Thread):
    def __init__(self, duration):
        self.data = data
        Thread.__init__(self)

    def run(self):
        while True:
            time_to_stop = reminder(duration)
            time.sleep(self.duration)
            current_time = datetime.now()
            print('notification sent to user ')
            if time_to_stop == current_time:
                break
        
        for conn in connections:
            conn.close()

# create new thread to call api

# On a separate note, if you are using uWSGI in deployment, you need to add

# --enable-threads
# argument to enable multi threading.