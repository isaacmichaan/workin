import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', 7979))
server.listen(2)

while True:
	conn, addr = server.accept()
	f = open("ls", "wb")
	while True:
		data = conn.recv(1024)
		if not data:
			break
		f.write(data)
	f.close()
