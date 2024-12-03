#time module in if else condition
import time
ts= int(time.strftime('%H'))
print("current time is",ts)
if (ts>0 and ts<12):
    print ("good morning sir")
elif(ts>=12 and ts<18):
    print ("good afternoon sir")
else:
    print ("good evening sir")