import socket
import threading

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.client = None
        self.message = ""

    def stream(self):
        while True:
            self.client.send(self.message.encode('utf-8'))

    # Main function to receive the clients connection
    def run(self):
        while True:
            print('Server is running and listening ...')
            self.client, address = self.server.accept()
            print(f'Connection is established with {str(address)}')
            thread = threading.Thread(target=self.stream)
            thread.start()

server = Server('192.168.178.30', 8001)
server.run()