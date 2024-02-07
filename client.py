import socket
import pygame

HOST = "192.168.178.79"
PORT = 8001

screen = pygame.display.set_mode((640, 360))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            key = pygame.key.get_pressed()
            if key[pygame.K_w]: s.sendall("w".encode())
            elif key[pygame.K_s]: s.sendall("s".encode())
            elif key[pygame.K_a]: s.sendall("a".encode())
            elif key[pygame.K_d]: s.sendall("d".encode())
        except KeyboardInterrupt:
            s.close()
            break