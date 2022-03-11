import socket
#import a library called socket

#address of server we would like to listen
serverPort = 23120
serverName = 'localhost'
#reserved address for local in python
serverAddress = (serverName, serverPort)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#there are different types of sockets we can request
#tcp vs. udp
serverSocket.bind(serverAddress)
#associate server addres with this fresh socket
serverSocket.listen(1)

#some message for possible debugging:
print("server is listening")
client_socket, addr =serverSocket.accept()
#beyond this point, connection is established,
#and return value client_socket is the server end's handle
#of this socket for communicating payload
while client_socket.recv(2048):
  #process the message
#checking if message is a legit format
  #parse the http request header
  
  #send the modified message
  print("receiving packet")
    #set up a sentinel value, EOF, or -1

client_socket.close()
  
  
