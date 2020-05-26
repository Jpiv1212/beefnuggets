import pygame, random, sys, time, math
pygame.init()
disp = pygame.display.set_mode((1280,720))
class Player():
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.rotation = 0
player = Player()

class Thing():
    viewangle = .8
    
    def __init__(self, pos, image):
        self.image = image
        self.posx, self.posy = pos

    def render(self):
        y = (self.posy-player.posy+24.01)
        x = (self.posx-player.posx+24.01)
        angle = math.atan(x/y)+math.pi/2
        if y<0: angle+=math.pi
        beef = abs(angle-player.rotation)
        if beef < Thing.viewangle or beef>2*math.pi-Thing.viewangle:
            disp.blit(self.image, (640+self.posx-player.posx, 360+self.posy-player.posy))

things = []
##things.append(Thing((0,0),pygame.image.load("stuff\\freef.png").convert()))
for i in range(40):
    for j in range(40):
        things.append(Thing((i*48,j*48),pygame.image.load("stuff\\grass1.png").convert()))
t = time.time()
while True:
    disp.fill((0,0,0))
    nt = time.time()
    dt = nt-t
    print(nt-t)
    t = nt
##    print(player.rotation)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.posx -= 250*dt
    if keys[pygame.K_d]:
        player.posx += 250*dt
    if keys[pygame.K_w]:
        player.posy -= 250*dt
    if keys[pygame.K_s]:
        player.posy += 250*dt
    if keys[pygame.K_e]:
        player.rotation -= 2.5*dt
    if keys[pygame.K_q]:
        player.rotation += 2.5*dt
    player.rotation %= 2*math.pi

    for thing in things:
              thing.render()
    pygame.display.flip()
