
# SERVER SIDE
import socket
socket_ = socket.socket()
host = socket.gethostbyname()
port = 9999

socket_.bind((host, port))
socket_.listen(1)
while True :
    client_socket, addr = socket_.accept()

    print(f"Got a connection from {addr}")
    client_socket.send(b"I am listening")
    client_socket.close()

# CLIENT SIDE
import socket
socket1_ = socket.socket() 
host1 = socket.gethostname() 
port1 = 9999
socket1_.connect((host, port))
response = socket1_.recv(1024) 
socket1_.close() 
print(response)
