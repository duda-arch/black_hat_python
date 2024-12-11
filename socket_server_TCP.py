import socket
import threading


def main():
    
    host = "0.0.0.0"
    port = 3000

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(5)
    print(f'[*] Listening {host} {port}')
    
    while True:
        client,addr = server.accept()
        print(f'[*] connection accept {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
        

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Receiver : {request.decode('utf-8')}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()