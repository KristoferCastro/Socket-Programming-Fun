import socket
import sys

# same as server create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
port = 12345 # this has to be where the server is listenning to
server_address = (ip, port)
print >> sys.stderr, 'connecting to %s port %s' % server_address
# in the server we bind the server address to the socket
# in the client, we connect to the server.  We give the location 
# it can be found, and in that computer, the port number
sock.connect(server_address) 

try:
	# send data
	message = 'This is the message.  It will be repeated.'
	print >> sys.stderr, 'sending "%s"' % message
	sock.sendall(message)

	# look for response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >> sys.stderr, 'received "%s"' % data 
	
finally:
	print >> sys.stderr, 'closing socket'
	sock.close()
	



