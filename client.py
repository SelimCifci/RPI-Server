import socket

HOST = "192.168.178.30"
PORT = 8001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        try:
            s.sendall("Ping".encode())
            data = s.recv(1024).decode()
            print(data)
        except KeyboardInterrupt:
            break
    s.close()