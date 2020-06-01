import pygame, random, sys, time, math
pygame.init()
disp = pygame.display.set_mode((1280,720))#, pygame.FULLSCREEN)
class Player():
    models = [pygame.image.load("stuff\\player1.png").convert(),
              pygame.image.load("stuff\\player2.png").convert(),
              pygame.image.load("stuff\\player3.png").convert(),
              pygame.image.load("stuff\\player4.png").convert()]
    def __init__(self):
        self.posx = 960.01
        self.posy = 960.01
        self.rotation = 1.46
        for model in Player.models:
            model.set_colorkey((255,255,255))

    def render(self):
        step = int((self.rotation+math.pi/4)%(math.pi*2)//(math.pi/2))
        model = Player.models[step]
        disp.blit(model, ((640-model.get_width()//2,360-model.get_height()//2)))
player = Player()

class Thing():
    viewangle = .8
    
    def __init__(self, pos, image, solid = False):
        self.image = image
        self.posx, self.posy = pos
        self.solid = solid

    def render(self):
##        y = (self.posy-player.posy+24.01)
##        x = (self.posx-player.posx+24.01)
##        angle = math.atan(x/y)+math.pi/2
##        if y<0: angle+=math.pi
##        beef = abs(angle-player.rotation)
##        if beef < Thing.viewangle or beef>2*math.pi-Thing.viewangle:
        disp.blit(self.image, (640+self.posx-player.posx, 360+self.posy-player.posy))
        return self.solid

##things = []
grasses = [pygame.image.load("stuff\\grass1.png").convert(),pygame.image.load("stuff\\grass2.png").convert(),pygame.image.load("stuff\\grass3.png").convert()]
walls = [pygame.image.load("stuff\\wall1.png").convert(),pygame.image.load("stuff\\wall2.png").convert(),pygame.image.load("stuff\\wall3.png").convert()]
##things.append(Thing((0,0),pygame.image.load("stuff\\freef.png").convert()))
##for i in range(40):
##    things.append([])
##    for j in range(40):
##        things[i].append(Thing((i*48,j*48),random.choice(grasses)))
##
##for i in range(10,30):
##    things[i][30] = Thing((i*48,30*48),pygame.image.load("stuff\\wall.png").convert(), True)
##    things[i][10] = Thing((i*48,10*48),pygame.image.load("stuff\\wall.png").convert(), True)
##    things[10][i] = Thing((10*48,i*48),pygame.image.load("stuff\\wall.png").convert(), True)
##    things[30][i] = Thing((30*48,i*48),pygame.image.load("stuff\\wall.png").convert(), True)
##
##for i in range(18,22):
##    things[30][i] = Thing((30*48,i*48),random.choice(grasses))

tiles = {(127,127,127,255):(walls, True),
         (34,177,76,255):(grasses, False)}

def loadlevel(filename):
    mapp = pygame.image.load(filename).convert()
    w,h = mapp.get_size()
    out = []
    for j in range(h):
        out.append([])
        for i in range(w):
            color = tuple(mapp.get_at((j,i)))
            out[j].append(Thing((j*48,i*48),random.choice(tiles[color][0]),tiles[color][1]))
    return out

def loadlevel2(filename):
    mapp = pygame.image.load(filename).convert()
    w,h = mapp.get_size()
    out = []
    for j in range(h*2):
        out.append([None]*(w*2))
    for j in range(h):
        for i in range(w):
            color = tuple(mapp.get_at((j,i)))
            tile = random.choice(tiles[color][0])
            solid = tiles[color][1]
            out[2*j][2*i] = Thing((j*48,i*48),tile.subsurface((0,0,24,24)),solid)
            out[2*j+1][2*i] = Thing((j*48+24,i*48),tile.subsurface((24,0,24,24)),solid)
            out[2*j][2*i+1] = Thing((j*48,i*48+24),tile.subsurface((24,0,24,24)),solid)
            out[2*j+1][2*i+1] = Thing((j*48+24,i*48+24),tile.subsurface((24,24,24,24)),solid)
    return out

def loadlevel3(filename):
    mapp = pygame.image.load(filename).convert()
    w,h = mapp.get_size()
    out = []
    for j in range(h*4):
        out.append([None]*(w*4))
    for j in range(h):
        for i in range(w):
            color = tuple(mapp.get_at((j,i)))
            tile = random.choice(tiles[color][0])
            solid = tiles[color][1]
            out[4*j][4*i] = Thing((j*48,i*48),tile.subsurface((0,0,12,12)),solid)
            out[4*j+1][4*i] = Thing((j*48+12,i*48),tile.subsurface((12,0,12,12)),solid)
            out[4*j+2][4*i] = Thing((j*48+24,i*48),tile.subsurface((24,0,12,12)),solid)
            out[4*j+3][4*i] = Thing((j*48+36,i*48),tile.subsurface((36,0,12,12)),solid)
            out[4*j][4*i+1] = Thing((j*48,i*48+12),tile.subsurface((0,12,12,12)),solid)
            out[4*j+1][4*i+1] = Thing((j*48+12,i*48+12),tile.subsurface((12,12,12,12)),solid)
            out[4*j+2][4*i+1] = Thing((j*48+24,i*48+12),tile.subsurface((24,12,12,12)),solid)
            out[4*j+3][4*i+1] = Thing((j*48+36,i*48+12),tile.subsurface((36,12,12,12)),solid)
            out[4*j][4*i+2] = Thing((j*48,i*48+24),tile.subsurface((0,24,12,12)),solid)
            out[4*j+1][4*i+2] = Thing((j*48+12,i*48+24),tile.subsurface((12,24,12,12)),solid)
            out[4*j+2][4*i+2] = Thing((j*48+24,i*48+24),tile.subsurface((24,24,12,12)),solid)
            out[4*j+3][4*i+2] = Thing((j*48+36,i*48+24),tile.subsurface((36,24,12,12)),solid)
            out[4*j][4*i+3] = Thing((j*48,i*48+36),tile.subsurface((0,36,12,12)),solid)
            out[4*j+1][4*i+3] = Thing((j*48+12,i*48+36),tile.subsurface((12,36,12,12)),solid)
            out[4*j+2][4*i+3] = Thing((j*48+24,i*48+36),tile.subsurface((24,36,12,12)),solid)
            out[4*j+3][4*i+3] = Thing((j*48+36,i*48+36),tile.subsurface((36,36,12,12)),solid)
    return out

def loadlevel4(filename):
    mapp = pygame.image.load(filename).convert()
    w,h = mapp.get_size()
    out = []
    for j in range(h*4):
        out.append([None]*(w*4))
    for j in range(h):
        for i in range(w):
            color = tuple(mapp.get_at((j,i)))
            tile = random.choice(tiles[color][0])
            solid = tiles[color][1]
            if not solid:
                out[4*j][4*i] = Thing((j*48,i*48),tile.subsurface((0,0,12,12)),solid)
                out[4*j+1][4*i] = Thing((j*48+12,i*48),tile.subsurface((12,0,12,12)),solid)
                out[4*j+2][4*i] = Thing((j*48+24,i*48),tile.subsurface((24,0,12,12)),solid)
                out[4*j+3][4*i] = Thing((j*48+36,i*48),tile.subsurface((36,0,12,12)),solid)
                out[4*j][4*i+1] = Thing((j*48,i*48+12),tile.subsurface((0,12,12,12)),solid)
                out[4*j+1][4*i+1] = Thing((j*48+12,i*48+12),tile.subsurface((12,12,12,12)),solid)
                out[4*j+2][4*i+1] = Thing((j*48+24,i*48+12),tile.subsurface((24,12,12,12)),solid)
                out[4*j+3][4*i+1] = Thing((j*48+36,i*48+12),tile.subsurface((36,12,12,12)),solid)
                out[4*j][4*i+2] = Thing((j*48,i*48+24),tile.subsurface((0,24,12,12)),solid)
                out[4*j+1][4*i+2] = Thing((j*48+12,i*48+24),tile.subsurface((12,24,12,12)),solid)
                out[4*j+2][4*i+2] = Thing((j*48+24,i*48+24),tile.subsurface((24,24,12,12)),solid)
                out[4*j+3][4*i+2] = Thing((j*48+36,i*48+24),tile.subsurface((36,24,12,12)),solid)
                out[4*j][4*i+3] = Thing((j*48,i*48+36),tile.subsurface((0,36,12,12)),solid)
                out[4*j+1][4*i+3] = Thing((j*48+12,i*48+36),tile.subsurface((12,36,12,12)),solid)
                out[4*j+2][4*i+3] = Thing((j*48+24,i*48+36),tile.subsurface((24,36,12,12)),solid)
                out[4*j+3][4*i+3] = Thing((j*48+36,i*48+36),tile.subsurface((36,36,12,12)),solid)
            else:
                thing = Thing((j*48,i*48),tile,solid)
                out[4*j][4*i] = thing
                out[4*j+1][4*i] = thing
                out[4*j+2][4*i] = thing
                out[4*j+3][4*i] = thing
                out[4*j][4*i+1] = thing
                out[4*j+1][4*i+1] = thing
                out[4*j+2][4*i+1] = thing
                out[4*j+3][4*i+1] = thing
                out[4*j][4*i+2] = thing
                out[4*j+1][4*i+2] = thing
                out[4*j+2][4*i+2] = thing
                out[4*j+3][4*i+2] = thing
                out[4*j][4*i+3] = thing
                out[4*j+1][4*i+3] = thing
                out[4*j+2][4*i+3] = thing
                out[4*j+3][4*i+3] = thing
    return out

things = loadlevel4("stuff\\test.png")

incrementors = ((1,1),(-1,1),(1,-1),(-1,-1))
def raycast(slope, d):
    x,y = player.posx/12,player.posy/12
    if slope > 0:
        if d > 0:
            c = math.ceil(x),math.ceil(y)
        else:
            c = math.floor(x),math.floor(y)
    else:
        if d > 0:
            c = math.ceil(x),math.floor(y)
        else:
            c = math.floor(x),math.ceil(y)
    cx,cy = c
    try:things[math.floor(x)][math.floor(y)].render()
    except Exception as e:
        return
    if abs((c[1]-y)/(c[0]-x))<abs(slope):
        oy = y
        y += d*abs(c[0]-x)*slope
        try:
            if y > cy:
                while cy < y:
                    if things[math.floor(x)][cy].render(): return
                    cy+=1
            else:
                while cy > y:
                    cy -= 1
                    if cy < 0 or things[math.floor(x)][cy].render(): return
##            for y2 in range(math.floor(min(oy,y)),math.ceil(max(oy,y)),1):
##                things[int(x)][int(y2)].render()
        except: pass
        else:
            x = c[0]
##            print("Beef")
            rayx(d, slope, x, y, 0)
    else:
        ox = x
        x += d*abs((c[1]-y)/slope)
        try:
            if x > cx:
                while cx < x:
                    if things[cx][math.floor(y)].render(): return
                    cx += 1
            else:
                while cx > x:
                    cx -= 1
                    if cx < 0 or things[cx][math.floor(y)].render(): return
##            for x2 in range(math.floor(min(ox,x)),math.ceil(max(ox,x)),1):
##                things[int(x2)][int(y)].render()
        except: pass
        else:
            y = c[1]
            rayy(d, slope, x, y, 0)

def rayx(d, slope, x, y, e):
##    if e > 50:
##        return
##    e += 1
    if d*slope < 0:
        cy = math.floor(y)
    else:
        cy = math.ceil(y)
    cx = x
    x += d*abs((cy-y)/slope)
    try:
        if x > cx:
            while cx < x:
                if things[cx][math.floor(y)].render(): return
                cx += 1
        else:
            while cx > x:
                cx -= 1
                if cx < 0 or things[cx][math.floor(y)].render(): return
##            for x2 in range(math.floor(min(ox,x)),math.ceil(max(ox,x)),1):
##                things[int(x2)][int(y)].render()
    except: pass
    else:
        if abs(player.posx-x*12) > 640: return
        y = cy
        rayy(d, slope, x, y, e)

def rayy(d, slope, x, y, e):
##    if e > 50:
##        return
##    e += 1
    if d < 0:
        cx = math.floor(x)
    else:
        cx = math.ceil(x)
    oy = y
    y += d*abs(cx-x)*slope
    try:
        if y > oy:
            while oy < y:
                if things[math.floor(x)][oy].render(): return
                oy+=1
        else:
            while oy > y:
                oy -= 1
                if oy < 0 or things[math.floor(x)][oy].render(): return
##            for y2 in range(math.floor(min(oy,y)),math.ceil(max(oy,y)),1):
##                things[int(x)][int(y2)].render()
    except: pass
    else:
        if abs(player.posy-y*12) > 360: return
        x = cx
##            print("Beef")
        rayx(d, slope, x, y, e)

span = 36
##span = 58
turnspeed = 3
mouseangle = 0
clock = pygame.time.Clock()
clock.tick()
font = pygame.font.SysFont(pygame.font.get_default_font(), 60)
while True:
    disp.fill((0,0,0))
    dt = clock.tick(40)/1000
##    print(nt-t)
##    print(player.rotation)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_DOWN:
                span -= 1
            elif event.key == pygame.K_UP:
                span += 1
        elif event.type == pygame.MOUSEMOTION:
            mx, my = event.pos
            if mx == 640:
                if my > 0:
                    mouseangle = 0
                else:
                    mouseangle = math.pi
            else:
                mouseangle = math.atan(-(my-360)/(mx-640))+math.pi/2
            if mx < 640: mouseangle += math.pi
    peef = player.rotation-mouseangle
    if peef >= math.pi: peef -= 2*math.pi
    if peef <= -math.pi: peef += 2*math.pi
    if abs(peef) <= turnspeed*dt or abs(peef)>=2*math.pi-turnspeed*dt:
        player.rotation = mouseangle
    else:
        player.rotation -= turnspeed*dt*peef/abs(peef)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.posx -= 250*dt
    if keys[pygame.K_d]:
        player.posx += 250*dt
    if keys[pygame.K_w]:
        player.posy -= 250*dt
    if keys[pygame.K_s]:
        player.posy += 250*dt
##    if keys[pygame.K_e]:
##        player.rotation -= 2.5*dt
##    if keys[pygame.K_q]:
##        player.rotation += 2.5*dt
    player.rotation %= 2*math.pi
    if player.rotation < math.pi:
        d = 1
    else:
        d = -1
##    print(player.rotation,1/math.tan(player.rotation))
    for i in range(-span,span+1):
        angle = (player.rotation+i/span*math.pi/3)%(2*math.pi)
        if angle < math.pi:
            cd = 1
        else:
            cd = -1
        if angle == 0: angle = 0.001
        if angle == math.pi: angle = math.pi+0.001
        raycast(1/math.tan(angle),cd)
    for i in range(-span,span+1):
        angle = (player.rotation+i/span*math.pi/3)%(2*math.pi)
        if angle < math.pi:
            cd = 1
        else:
            cd = -1
##        pygame.draw.line(disp, (255,0,0), (640,360), (640+2000*cd, 360+2000/math.tan(angle)*cd))
##    for thing in things:
##              thing.render()

    player.render()
            
    fps = font.render(str(round(10*clock.get_fps())/10),False,(255,0,0))
    disp.blit(fps, (24,24))
    pygame.display.flip()
