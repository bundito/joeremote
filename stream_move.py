import os
import subprocess
from subprocess import PIPE, Popen
import threading
import socket
import asyncio
import time
import pika

def move(data):

    print("Module imported.")

    credentials = pika.PlainCredentials('bundito', 'D1t0rabbit01')
    parameters = pika.ConnectionParameters(credentials=credentials)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.0.0.53',
                                                                   port=5672,
                                                                   virtual_host='/',
                                                                   credentials=credentials,
                                                                    ))
    channel = connection.channel()

    channel.queue_declare(queue='soviet', durable=True)

    channel.basic_publish(exchange='',
                          routing_key='soviet',
                          body='START')


    print("After move entry point")

    title = "X2 (2003).mp4"
    testpath = os.path.join("/home/bundito/Downloads", title)
    if os.path.exists(testpath):
        dest = os.path.join("/media/Movies")
        orig = testpath
    else:
        dest = testpath
        orig = os.path.join("/media/Movies", title)


    with Popen(["rsync", "-avz", "--remove-source-files", "--info=progress2", orig, dest], bufsize=1, universal_newlines = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
        for line in p.stdout:
          #  xmit(line)
            print(line, end='')
            channel.basic_publish(exchange='',
                                  routing_key='soviet',
                                  body=line)



    return("EOF")

