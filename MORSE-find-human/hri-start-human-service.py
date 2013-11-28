import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 4000))
s.send("id1 human move (1.0, 1.6)\n")
