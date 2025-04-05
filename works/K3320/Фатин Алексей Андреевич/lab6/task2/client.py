import socket 

def client():
    host = socket.gethostname()
    port = 5001

    socket_instance = socket.socket()
    socket_instance.connect((host, port))

    data=socket_instance.recv(1024).decode('utf-8')
    print(data)
    a = input('>>')
    socket_instance.send(a.encode('utf-8'))

    data=socket_instance.recv(1024).decode('utf-8')
    print(data)
    b = input('>>')
    socket_instance.send(b.encode('utf-8'))

    data=socket_instance.recv(1024).decode('utf-8')
    print(data)
    c = input('>>')
    socket_instance.send(c.encode('utf-8'))

    data=socket_instance.recv(1024).decode('utf-8')
    print(data)
    
    socket_instance.close()

if __name__ == '__main__':
    client()