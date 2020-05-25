import pygame, random, sys

pygame.init()
disp = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
disp.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
    pygame.display.flip()
