# import threading
# x = []
#
# while True:
#         user_input = input('Введи цифру: ')
#         if user_input == 'q':
#             break
#         x.append(int(user_input))
# print(x)
#
# def sum_up(f):
#     total = 0
#     for i in f:
#         total += i
#     print(total)
#
# def avg(f):
#     total = 0
#     for i in f:
#         total += i
#     avg_up = total / len(f)
#     print(avg_up)
#
#
#
# sum_threading = threading.Thread(target=sum_up, args=(x,))
# avg_threading = threading.Thread(target=avg, args=(x,))
#
# sum_threading.start()
# avg_threading.start()
#
# sum_threading.join()
# avg_threading.join()





import socket

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f'Listening {host}:{port}...')

    while True:
        conn, address = server_socket.accept()
        print(f'Successfully connected with {address}')

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f'Client {data=}')
            message = input('--->')
            conn.send(message.encode())

        conn.close()
        print('Connection was broken hard')

if __name__ == '__main__':
    start_server()












