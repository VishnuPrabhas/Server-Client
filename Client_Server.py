# -*- coding: utf-8 -*-
"""
@author: VishnuPrabhas
"""

# Server

import socket # Import socket module

s = socket.socket() # Create a Socket object
print('Socket successfully created')
port = 56789 # Reserve a port for service
s.bind(('', port)) # Bind to the port
print(f'socket bind to port {port}')
s.listen(5) # Wait for client connection
print('Socket is listening')
while True:
    c, addr = s.accept() # Establish connection with client
    print('Got connection from', addr)
    message = ('Thank you for connecting, The first server-client connection')
    c.send(message.encode())

    c.close() # Close the connection

 
# Client

import socket 

s = socket.socket() # Create a socket object
port = 56789 # Reserve the port for service 
s.connect(('127.0.0.1', port))
print(s.recv(1024))

s.close() # close the socket when done
