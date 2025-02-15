import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")

#socket.AF_INET is the address for IPv4. The socket type is SOCK_STREAM for TCP
#for IPv6, use socket.AF_INET6
# The socket type SOCK_DGRAM is for UDP

#socket.SOCK_STREAM is the socket type for TCP connection. which is reliable and connection oriented protocol.
#if you want to use UDP, use socket.SOCK_DGRAM

#listen()
 # puts the socket into listening mode. It can accept connections from clients.
s.listen(5)
print("Socket is listening") # the value 5 is the maximum number of queued connections
 