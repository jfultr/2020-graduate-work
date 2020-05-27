import socket
import serialcom

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 1234))
s.listen(5)


def run_server():
    while True:
        clientsocket, address = s.accept()
        print(f'Connection from {address}')
        clientsocket.send(bytes("Welcome to the server", "utf-8"))
        msg = clientsocket.recv(1024)
        print(msg)
        if msg:
            serialcom.push_position(0, 0, 0, 0, 200, 200)
        clientsocket.close()


if __name__ == '__main__':
    run_server()