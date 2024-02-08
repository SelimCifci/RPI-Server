import socket
import pygame

HOST = "192.168.178.79"
PORT = 8001

screen = pygame.display.set_mode((640, 360))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            send = "n"
            key = pygame.key.get_pressed()
            if key[pygame.K_w]: send = "w"
            elif key[pygame.K_s]: send = "s"
            elif key[pygame.K_a]: send = "a"
            elif key[pygame.K_d]: send = "d"

            s.sendto(send.encode(), (HOST, PORT))
        except KeyboardInterrupt:
            s.close()
            break