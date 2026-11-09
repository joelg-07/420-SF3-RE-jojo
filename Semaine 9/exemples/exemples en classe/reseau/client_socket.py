import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("10.50.11.30", 8080))
    client.sendall(b"Ceci est un test")
