import socket

HOST = "192.168.178.30"
PORT = 8001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                data = conn.recv(1024).decode()
                if data == "w": print("NACH VORNE DU FETTARSCH")
                elif data == "s": print("NACH VORNE DU FETTARSCH")
                elif data == "a": print("NACH VORNE DU FETTARSCH")
                elif data == "d": print("NACH VORNE DU FETTARSCH")
            except KeyboardInterrupt:
                break
        s.close()