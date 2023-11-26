import  socket

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input('------------->')

    while message.lower().strip() != 'quit':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f'server {data=}')
        message = input('-----> ')

    client_socket.close()

if __name__ == '__main__':
    start_client()