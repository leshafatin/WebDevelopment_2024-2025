import socket
import math


class Server:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def getRoots(self, a, b, c):
        d = b ** 2 - 4 * a * c 

        print(d)

        if d < 0:
            return None, None
        elif d == 0:
            x = (-b + math.sqrt(d)) / 2 * a
            return x, x
        else:
            x1 = (-b + math.sqrt(d) ) / (2 * a)
            x2 = (-b - math.sqrt(d) ) / (2 * a)
            return x1, x2

    def send(self, msg):
        self.conn.send(msg.encode('utf-8'))

    def receive(self):
        data = self.conn.recv(1024)
        return data.decode('utf-8')

    def start(self):
        self.sock.bind(('', 5001))
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()

    def close(self):
        self.sock.close()


def main():
    srv = Server()
    srv.start()

    srv.send("Input a: ")
    a = float(srv.receive())

    srv.send("Input b: ")
    b = float(srv.receive())

    srv.send("Input c: ")
    c = float(srv.receive())

    x1, x2 = srv.getRoots(a, b, c)
    srv.send(f"Roots of the eq is {x1, x2}")

    srv.close()


if __name__ == '__main__':
    main()