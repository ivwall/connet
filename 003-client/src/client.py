
import socket

clientSocket = socket.socket(socket.AF_INET, socklet.SOCK_STREAM)
clientSocket.send("Hello Server".encode())

dataFromServer = clientSocket.recv(1024)
print(dataFromServer.decode())


