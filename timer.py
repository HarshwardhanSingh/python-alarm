from subprocess import call
from datetime import datetime
from threading import Timer

a = datetime.today()
b = a.replace(day=int(raw_input("Enter Day: ")), hour=int(raw_input("Enter Hour: ")), minute=int(raw_input("Enter Minute: ")), second=0, microsecond=0)
difference_t =  b-a

secs=difference_t.seconds
	
def repeat():
	call(["cvlc","/home/odd/Music/abc.mp3"])
    
t = Timer(secs, repeat)
t.start()