from sseclient import SSEClient
import sys
host = 'localhost'
port = 5000
subcribe ='stream'
if(len(sys.argv) >4):
   subcribe = sys.argv[4]
if(len(sys.argv) >3):
   port = int(sys.argv[3])
if(len(sys.argv) >2):
   host = sys.argv[2]
messages = SSEClient('http://'+host+':'+str(port)+'/'+subcribe)
for msg in messages:
    print(str(msg)+'----'+sys.argv[1])
