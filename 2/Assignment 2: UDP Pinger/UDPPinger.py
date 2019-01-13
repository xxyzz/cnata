from socket import socket, AF_INET, SOCK_DGRAM, timeout
import time
serverName = "192.168.1.3"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

print("PING " + serverName)

for i in range(1, 11):
    clientSocket.sendto("ping".encode(), (serverName, serverPort))
    sendTime = time.time()
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        receiveTime = time.time()
        print("seq=%d time=%.3f ms" % (i, (receiveTime - sendTime) * 1000))
    except timeout:
        print("seq=%d timeout" % i)

clientSocket.close()
