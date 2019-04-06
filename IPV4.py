import socket
userinput = input("give me the damn address: ")
sock = socket.gethostbyname(userinput)
print ("the damn IPV4 of the address is " + sock);