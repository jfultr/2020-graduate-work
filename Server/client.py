import socket


def set_angles(angles):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('169.254.49.227', 1234))

    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    # left back, right back, left front, right front, second left, second right
    s.send(bytes(angles, "utf-8"))