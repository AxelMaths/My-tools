#!/usr/bin/python3           # This is client.py file from https://tutoriels.edu.lat/pub/python3/python-networking/python-3-programmation-reseau

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     

s.close()
print (msg.decode('ascii'))
