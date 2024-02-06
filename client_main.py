from client import Client
import pygame

pygame.init()
res = (640,360)
screen = pygame.display.set_mode(res)

client = Client('192.168.178.30', 8001)
client.run()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #array = list(client.recv)
    #img = pygame.image.frombuffer(array.data, res, 'RGB')
    #screen.blit(img, (0, 0))

    key = pygame.key.get_pressed()
    if key[pygame.K_w]: client.message = "w"
    if key[pygame.K_s]: client.message = "s"
    if key[pygame.K_a]: client.message = "a"
    if key[pygame.K_d]: client.message = "d"

    pygame.display.flip()