import time

def has_15_seconds_passed(start_time=None):
    if time.time() - start_time >= 15:  # Check if 15 seconds have passed
        return True
    else:
        return False