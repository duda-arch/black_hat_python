import socket

host = "0.0.0.0"
port = 3000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

data = client.recv(4096)

print(data.decode())

client.close()