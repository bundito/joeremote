import os
import subprocess
from subprocess import PIPE, Popen
import json
import time
import shutil
import zmq

import joe_destination

def move(data):

    print("Module imported.")

    print(data)

    paths = joe_destination.get_dest(data)
    orig = paths[0]
    dest = paths[1]
    folder_del = paths[2]

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://10.0.0.53:5555")


    with Popen(["rsync", "-avz", "--remove-source-files", "--info=progress2", orig, dest], bufsize=1, universal_newlines = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
        for line in p.stdout:
            print(line, end='')
            socket.send_string(line)

    time.sleep(1.5)
    if folder_del:
        print(folder_del)
        shutil.rmtree(folder_del)

    return("EOF")

