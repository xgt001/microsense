import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.0.103' # Get local machine name
port = 4000                # Reserve a port for your service.
s.connect((host, port))

while 1:
	streamer = s.recv(1024)
	if not streamer:
		break
	print streamer
s.close  