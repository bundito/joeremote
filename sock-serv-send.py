import sys
from socket import *
serverhost = "10.0.0.135"
serverport = 10000

message = [b'Hello network world']

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverhost, serverport))

for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print('Client recieved: ', data)

sockobj.close()