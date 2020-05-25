import pygame, random, sys, time, math
pygame.init()
disp = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
class Player():
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.rotation = 0
player = Player()

class Thing():
    def __init__(self, pos, image):
        self.image = image
##        self.image.convert()
        self.posx, self.posy = pos

    def render(self):
        if math.sin(player.rotation)*(self.posy-player.posy+24)+math.cos(player.rotation)*(self.posx-player.posx+24) >= .5*((self.posy-player.posy+24)**2+(self.posx-player.posx+24)**2)**.5:
            disp.blit(self.image, (640+self.posx-player.posx, 360+self.posy-player.posy))

things = []
##things.append(Thing((0,0),pygame.image.load("stuff\\freef.png").convert()))
for i in range(20):
    for j in range(20):
        things.append(Thing((i*48,j*48),pygame.image.load("stuff\\grass1.png").convert()))
t = time.time()
while True:
    disp.fill((0,0,0))
    nt = time.time()
    print(nt-t)
    t = nt
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.posx -= 5
    if keys[pygame.K_d]:
        player.posx += 5
    if keys[pygame.K_w]:
        player.posy -= 5
    if keys[pygame.K_s]:
        player.posy += 5
    if keys[pygame.K_e]:
        player.rotation += .05
    if keys[pygame.K_q]:
        player.rotation -= .05

    for thing in things:
              thing.render()
    pygame.display.flip()
