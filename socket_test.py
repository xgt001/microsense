import socket               # Import socket module


def printer(message):
  print "Got your signal bro"+message
 


def socket_launcher():
    s = socket.socket()         # Create a socket object
    host = '192.168.0.103' # Get local machine name
    port = 4000                # Reserve a port for your service.
    s.connect((host, port))
    while 1:
	    global streamer
	    streamer = s.recv(1024)
	    if not streamer:
		    break
	    #print streamer
	    printer(streamer)
    s.close  
  

  
if __name__ == '__main__':
  socket_launcher()
  # print streamer