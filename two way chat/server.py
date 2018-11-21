import socket
s = socket.socket()
s.bind((socket.gethostname(), 1234))
s.listen(5)

import threading
class Send(threading.Thread):
    def run(self):
        while True:
            string = input()
            c.send(string.encode())
class Recv(threading.Thread):
    def run(self):
        while True:
            print(c.recv(1024))

c, addr = s.accept()
Send().start()
Recv().start()