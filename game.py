import pygame, random, sys, time, math
pygame.init()
disp = pygame.display.set_mode((1280,720))
class Player():
    def __init__(self):
        self.posx = 960.01
        self.posy = 960.01
        self.rotation = 1.46
player = Player()

class Thing():
    viewangle = .8
    
    def __init__(self, pos, image):
        self.image = image
        self.posx, self.posy = pos

    def render(self):
##        y = (self.posy-player.posy+24.01)
##        x = (self.posx-player.posx+24.01)
##        angle = math.atan(x/y)+math.pi/2
##        if y<0: angle+=math.pi
##        beef = abs(angle-player.rotation)
##        if beef < Thing.viewangle or beef>2*math.pi-Thing.viewangle:
        disp.blit(self.image, (640+self.posx-player.posx, 360+self.posy-player.posy))

things = []
grasses = [pygame.image.load("stuff\\grass1.png").convert(),pygame.image.load("stuff\\grass2.png").convert(),pygame.image.load("stuff\\grass3.png").convert()]
##things.append(Thing((0,0),pygame.image.load("stuff\\freef.png").convert()))
for i in range(40):
    things.append([])
    for j in range(40):
        things[i].append(Thing((i*48,j*48),random.choice(grasses)))

incrementors = ((1,1),(-1,1),(1,-1),(-1,-1))
def raycast(slope, d):
    x,y = player.posx/48,player.posy/48
    if slope > 0:
        if d > 0:
            i = incrementors[0]
            c = math.ceil(x),math.ceil(y)
        else:
            i = incrementors[3]
            c = math.floor(x),math.floor(y)
    else:
        if d > 0:
            i = incrementors[1]
            c = math.floor(x),math.ceil(y)
        else:
            i = incrementors[2]
            c = math.ceil(x),math.floor(y)
    if abs((c[1]-y)/(c[0]-x))<abs(slope):
        oy = y
        y += d*abs(c[0]-x)*slope
        print("change:",y-oy)
        try:
            for y2 in range(int(oy),math.ceil(y),d):
##                print(int(y2),int(x))
                things[int(x)][int(y2)].render()
        except: pass
        else:
            x = c[0]
    else:
        ox = x
        x += d*(c[1]-y)/slope
        try:
            for x2 in range(int(ox),math.ceil(x),d):
##                print(int(y),int(x2))
                things[int(x2)][int(y)].render()
        except: pass
        else:
            y = c[1]
    

t = time.time()
while True:
    disp.fill((0,0,0))
    nt = time.time()
    dt = nt-t
##    print(nt-t)
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
    if player.rotation < math.pi:
        d = 1
    else:
        d = -1
##    print(player.rotation,1/math.tan(player.rotation))
    raycast(1/math.tan(player.rotation),d)
    pygame.draw.line(disp, (255,0,0), (640,360), (640+48*d, 360+48/math.tan(player.rotation)*d))
##    for thing in things:
##              thing.render()
    pygame.display.flip()
