import datetime
import os
import uuid
import sys

SERVICE_NAME = "currency-exchange"
pid = os.getpid()
request_id = uuid.uuid4()
myhost = os.uname()[1] ### not portable

def log(message):
    print ("{}\t{}\t{}\t{}\t{}\t{}" .format (datetime.datetime.today(),
                        SERVICE_NAME,
                        pid,
                        request_id,
                        myhost, 
                        message),
                        file=sys.stderr)
                