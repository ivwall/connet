# stackoverflow.com/questions/50360680/can-you-use-python-sockets-for-docker-container-communicationun()
# pythontic.com/modules/socket/send
import socket

def receive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",4000))
    s.listen(2)

    while(True)
        conn, addr = s.accept()
        print("accepted from %s:%s"(addr[0],addr[1]))
        print(bytes.decode(conn.recv(1024)))
        conn.send("Hello Client.".encode())

