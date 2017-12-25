import os
import subprocess
from subprocess import PIPE, Popen
import pika
import threading

def move():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.0.0.135', port=9998,
                                                    blocked_connection_timeout=2000,
                                                    connection_attempts=10000))
    channel = connection.channel()
    channel.queue_declare(queue='soviet')
    channel.basic_publish(exchange='', routing_key='soviet', body='BEGIN')
    channel.queue_declare()

    title = "X2 (2003).mp4"
    testpath = os.path.join("/home/bundito/Downloads", title)
    if os.path.exists(testpath):
        dest = os.path.join("/media/Movies")
        orig = testpath
    else:
        dest = testpath
        orig = os.path.join("/media/Movies", title)

    print("Running rsync")
    channel.basic_publish(exchange='', routing_key='soviet', body='Starting rsync')

    with Popen(["rsync", "-avz", "--remove-source-files", "--info=progress2", orig, dest], bufsize=1, universal_newlines = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
        for line in p.stdout:
            print(line, end='')

            channel.basic_publish(exchange='', routing_key='soviet', body=line)

            print(line)


        connection.close()


