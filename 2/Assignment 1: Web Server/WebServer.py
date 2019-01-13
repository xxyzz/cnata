from socket import socket, AF_INET, SOCK_STREAM
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    httpMessage = connectionSocket.recv(1024).decode()
    firstLine = httpMessage.splitlines()[0]
    if firstLine == "GET / HTTP/1.1" or firstLine == "GET /index.html HTTP/1.1":
        with open('index.html') as f:
            read_data = f.read()
            header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\nContent-Length: %d\r\n\r\n" % len(read_data)
            connectionSocket.send(header.encode())
            connectionSocket.send(read_data.encode())
    else:
        with open('404.html') as f:
            read_data = f.read()
            header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nConnection: close\r\nContent-Length: %d\r\n\r\n" % len(read_data)
            connectionSocket.send(header.encode())
            connectionSocket.send(read_data.encode())
    connectionSocket.close()
