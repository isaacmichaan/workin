import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.0.2.4", 7979))
f = open("ls", "rb")
client.send(f.read())
f.close()
client.close()
#client.send(b"Hello Guys How Are You? :)")
