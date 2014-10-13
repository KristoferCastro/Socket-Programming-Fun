import socket
import sys

# This uses Internet Protocol Address (IPv4)
# So, when making a socket, you tell what kind of protocol
# to use and then the socket type.

# Socket Type is the transport layer protocol to use.
# Stream Socket: point-to-point delivery (in-order, reliable) uses TCP
# Datagram Socket: not point-to-point, UDP,
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
ip = 'localhost'
port = 12345
server_address = (ip, port)

print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# in java: Socket has a method called bind(SocketAddress bindpoint)

# once you created your socket, bind it to a port, wake
# it up to listen for connections
# the parameters says maximum number of queued connections
sock.listen(1) 

while True:
	# Wait for a connection
	print >> sys.stderr, 'waiting for a connection'
	# accept() returns an open connection
	# use recv() to read data, and sendall() to transmit
	connection, client_address = sock.accept() 

	# why is there a connection and client_address?
	# connection is where you read and send
	# client_address tells you information about the client
	
	try:
		print >> sys.stderr, 'connection from', client_address
		
		# Receive data in chunks and transmit it
		while True:
			chunk = 16
			data = connection.recv(chunk)
			if data:
				print >> sys.stderr, 'sending data back to client'
				connection.sendall(data)
			else:
				print >> sys.stderr, 'no more data from', client_address
				break
	finally:
		connection.close()
