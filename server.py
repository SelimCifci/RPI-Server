import socket
import Motor
import fcntl, os

HOST = "192.168.178.79"
PORT = 8001

pwm = Motor.Motor()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                data = conn.recv(1024).decode()
                if data.startswith("w"): pwm.setMotorModel(4096,4096,4096,4096)
                elif data.startswith("s"): pwm.setMotorModel(-4096,-4096,-4096,-4096)
                elif data.startswith("a"): pwm.setMotorModel(4096,4096,-4096,-4096)
                elif data.startswith("d"): pwm.setMotorModel(-4096,-4096,4096,4096)
            except socket.error:
                pwm.setMotorModel(0,0,0,0)
            except KeyboardInterrupt:
                s.close()
                break