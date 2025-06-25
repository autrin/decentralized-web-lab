import socket

s=socket.socket(); s.bind(("127.0.0.1", 9000)); s.listen(1)
conn,_=s.accept(); print(conn.recv(1024))