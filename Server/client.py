import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('169.254.49.227', 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))
s.send(bytes("0,0,0,0,0,0", "utf-8"))