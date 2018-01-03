from socket import *
myhost = "10.0.0.53"
myport = 10000

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myhost, myport))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()
    print('Server connected by ', address)
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(b'Echo => ' + data)
    connection.close()