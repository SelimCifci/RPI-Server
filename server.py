import socket
import Motor

HOST = "192.168.178.79"
PORT = 8001

pwm = Motor.Motor()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        try:
            data, _ = s.recvfrom(1024)
            data = data.decode()
            print(data)
            if data.startswith("w"): pwm.setMotorModel(4096,4096,4096,4096)
            elif data.startswith("s"): pwm.setMotorModel(-4096,-4096,-4096,-4096)
            elif data.startswith("a"): pwm.setMotorModel(4096,4096,-4096,-4096)
            elif data.startswith("d"): pwm.setMotorModel(-4096,-4096,4096,4096)
            elif data.startswith("n"): pwm.setMotorModel(0,0,0,0)
        except socket.error:
            pwm.setMotorModel(0,0,0,0)
        except KeyboardInterrupt:
            s.close()
            break