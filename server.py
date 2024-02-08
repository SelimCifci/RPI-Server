from omegaconf import DictConfig
import socket
import hydra
import Motor

@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig):
    pwm = Motor.Motor()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((cfg.HOST, cfg.PORT))
        while True:
            try:
                data, _ = s.recvfrom(1)
                data = data.decode()
                print(data)
                if data == "w": pwm.setMotorModel(4096,4096,4096,4096)
                elif data == "s": pwm.setMotorModel(-4096,-4096,-4096,-4096)
                elif data == "a": pwm.setMotorModel(4096,4096,-4096,-4096)
                elif data == "d": pwm.setMotorModel(-4096,-4096,4096,4096)
                elif data == "n": pwm.setMotorModel(0,0,0,0)
            except KeyboardInterrupt:
                s.close()
                break

if __name__ == '__main__':
    main()