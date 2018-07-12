# -*- coding: UTF-8 -*-
# import socket
# import json
# data ={'type':'userInit', 'uid': 1, 'name' : 'meinv', 'avatar' : ''}
# data_json = json.dumps(data)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('10.17.18.41', 8282))

import socket
import threading

import json

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        print ("Send: {}".format(message))
        sock.sendall(message)
        response = sock.recv(1024)
        jresp = json.loads(response)
        print ("Recv: ",jresp)

    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = '10.17.18.41', 8282
    msg1 = {'type':'userInit', 'uid': 1, 'name' : 'meinv', 'avatar' : ''}
    msg2 = {'type':'userInit', 'uid': 1, 'name' : 'meinv', 'avatar' : ''}
    msg3 = {'type':'userInit', 'uid': 2, 'name' : 'meinv', 'avatar' : ''}
    jmsg1 = json.dumps(msg1)
    jmsg2 = json.dumps(msg2)
    jmsg3 = json.dumps(msg3)

    client(HOST, PORT, jmsg1)
    client(HOST, PORT, jmsg2)
    client(HOST, PORT, jmsg3)