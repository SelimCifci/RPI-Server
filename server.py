import socket
import Motor

HOST = "192.168.178.79"
PORT = 8001

pwm = Motor.Motor()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                data = conn.recv(1024).decode()
                if data == "w": pwm.setMotorModel(4096,4096,4096,4096)
                elif data == "s": pwm.setMotorModel(-4096,-4096,-4096,-4096)
                elif data == "a": pwm.setMotorModel(4096,4096,-4096,-4096)
                elif data == "d": pwm.setMotorModel(-4096,-4096,4096,4096)
                elif data == "Stop": pwm.setMotorModel(0,0,0,0)
            except KeyboardInterrupt:
                break
        s.close()