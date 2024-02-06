import socket
import threading

class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.message = ""
        self.recv = ""

    def receive(self):
        while True:
            try:
                self.recv = self.client.recv(4096).decode('utf-8')
            except:
                print('Error!')
                self.client.close()
                break

    def send(self):
        old_message = None
        while True:
            if self.message != old_message:
                self.client.send(self.message.encode('utf-8'))
            old_message = self.message

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()