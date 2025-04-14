import socket

def server():
    host = socket.gethostname()
    port = 5001

    socket_instance = socket.socket()
    socket_instance.bind((host, port))

    socket_instance.listen(1)
    conn, address = socket_instance.accept()
    print("Connected: " + str(address))

    data = conn.recv(1024).decode()
    print("Client sent: " + str(data))

    response = "Hello, client"
    conn.send(response.encode())

    conn.close()

if __name__ == '__main__':
    server()