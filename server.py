import socket

s = socket.socket(); s.bind(("127.0.0.1", 9000)); s.listen(1)