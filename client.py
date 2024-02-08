import socket
import pygame

HOST = "192.168.178.30"
PORT = 6666

screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            key = pygame.key.get_pressed()
            if key[pygame.K_w]: s.sendto("w".encode(), (HOST, PORT))
            elif key[pygame.K_s]: s.sendto("s".encode(), (HOST, PORT))
            elif key[pygame.K_a]: s.sendto("a".encode(), (HOST, PORT))
            elif key[pygame.K_d]: s.sendto("d".encode(), (HOST, PORT))
        except KeyboardInterrupt:
            s.close()
            break

        clock.tick(30)