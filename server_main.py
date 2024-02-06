from picamera2 import Picamera2
from server import Server
import threading

res = (640,360)

camera = Picamera2()
camera.preview_configuration.main.size = res
camera.preview_configuration.main.format = 'BGR888'
camera.configure("preview")
camera.start()

server = Server('192.168.178.30', 8001)
thread = threading.Thread(target=server.run)
thread.start()

while True:
    try:
        #array = camera.capture_array()
        #server.message = str(array)
        print("A")
    except KeyboardInterrupt:
        break