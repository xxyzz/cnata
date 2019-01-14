from socket import socket, AF_INET, SOCK_STREAM
# import threading
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("The server is ready")

def proxy(connectionSocket):
    httpMessage = connectionSocket.recv(1024).decode()
    hostName = httpMessage.splitlines()[0].split(' ')[1][1:]
    try:
        with open(hostName) as f:
            read_data = f.read()
            header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\nContent-Length: %d\r\n\r\n" % len(read_data)
            connectionSocket.sendall(header.encode())
            connectionSocket.sendall(read_data.encode())
            connectionSocket.close()
            print("send cache file")
    except:
        proxySocket = socket(AF_INET, SOCK_STREAM)
        proxySocket.settimeout(5)
        try:
            proxySocket.connect((hostName, 80))
            httpRequest = 'GET / HTTP/1.1\r\nHost: ' + hostName + '\r\n\r\n'
            proxySocket.sendall(httpRequest.encode())
            data = b""
            try:
                while True:
                    segment = proxySocket.recv(2048)
                    if not segment:
                        break
                    data += segment
            except:
                data = data.decode()
                data = data[data.index("<!"):]
                proxySocket.close()
                with open(hostName, "w") as f:
                    f.write(data)
                header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\nContent-Length: %d\r\n\r\n" % len(data)
                connectionSocket.sendall(header.encode())
                connectionSocket.sendall(data.encode())
                connectionSocket.close()
                print("save then send")
        except:
            print("Unknown hostname: " + hostName)

while True:
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.settimeout(5)
    proxy(connectionSocket)
    # threading.Thread(target=proxy, args=connectionSocket)
