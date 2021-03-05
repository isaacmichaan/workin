# after client connect to server, we can set a command for client to return (like passwd)
#!/usr/bin/env python3
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8989))
server.listen()
print("Server Listening, Port:8989")

try:
	while True:
		conn, addr = server.accept()
		print("New Client")
		while True:
			command = input("Enter Command: ")
			if command == "exit":
				conn.send(b"exit")
				break
			conn.send(str.encode(command))
			#while True:
			data = conn.recv(1024) # there was a problem here, if client don't have anything to send so how to stop
				#if len(data) > 0:
			print(data.decode("utf-8"))
				#else:
					#break
		break
except:
	server.close()

server.close()
