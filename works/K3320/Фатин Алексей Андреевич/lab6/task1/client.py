import socket 

def client():
    host = socket.gethostname()
    port = 5001

    socket_instance = socket.socket()
    socket_instance.connect((host, port))

    message = "Hello, server"
    socket_instance.send(message.encode())

    data = socket_instance.recv(1024).decode()
    print('Server sent: ' + data)

    socket_instance.close()

if __name__ == '__main__':
    client()