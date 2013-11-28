import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 4000))
s.send("{'x' : 4.0, 'y': 2.0, 'z': 0.0, 'tolerance' : 0.5, 'speed' : 1.0}")
