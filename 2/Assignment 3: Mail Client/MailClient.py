from socket import socket, AF_INET, SOCK_STREAM, gethostname
import base64
serverName = "aspmx.l.google.com"
serverPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def sendAndprint(command):
    print(command)
    if (isinstance(command, str)):
        clientSocket.sendall(command.encode())
    else:
        clientSocket.sendall(command)
    serverResponse = clientSocket.recv(1024)
    print("From Server: ", serverResponse.decode())

serverResponse = clientSocket.recv(1024)
print("From Server: ", serverResponse.decode())
sendAndprint("HELO " + gethostname())
sendAndprint("AUTH LOGIN")
username = input("Username: ")
sendAndprint(base64.b64encode(username.encode()))
password = input("Password: ")
sendAndprint(base64.b64encode(password.encode()))
sendAndprint("MAIL FROM: <" + username + ">")
rcptTo = input("Rcpt To: ")
sendAndprint("RCPT TO: <" + rcptTo + ">")
sendAndprint("DATA")
data = input("Data: ")
sendAndprint(data)
sendAndprint("\r\n.\r\n")
sendAndprint("QUIT")

clientSocket.close()
