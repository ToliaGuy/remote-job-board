import datetime
import time

while True:
    # Get the current time
    now = datetime.datetime.now()
    # Get the current time in seconds
    now_seconds = now.hour * 3600 + now.minute * 60 + now.second

    # Sleep for 1 second
    time.sleep(1)