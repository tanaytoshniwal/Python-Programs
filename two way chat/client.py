import socket
s = socket.socket()
s.connect((socket.gethostname(), 1234))

import threading
class Send(threading.Thread):
    def run(self):
        while True:
            string = input()
            s.send(string.encode())
class Recv(threading.Thread):
    def run(self):
        while True:
            print(s.recv(1024))

Send().start()
Recv().start()