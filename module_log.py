import os
import datetime

def log_writer(msg, path=os.getcwd(), mode='a'):
    with open(path+"/hklog", mode) as hk_log:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        msg = f"{timestamp} - {msg}"
        hk_log.write(msg)