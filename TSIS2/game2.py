import pygame
import sys
pygame.init()
width=640
height=480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tank War")
screen = pygame.Surface((width,height))
bg = pygame.image.load("bg.jpg")
fps = pygame.time.Clock()

effect = pygame.mixer.Sound('move.wav')
effect.set_volume(0.08)

sound = pygame.mixer.Sound('hit.wav')
sound.set_volume(0.1)

Gameover_sound = pygame.mixer.Sound('NOOO.wav')

fire = pygame.mixer.Sound('fire.wav')
class Tank1():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.speed = 2
        self.bitmap = pygame.image.load(filename)
        self.const = self.bitmap
    
    def drawTank1(self):
        screen.blit(self.const,(self.x, self.y))
        return self.x, self.y
    
    def movementTank1(self, lastMove):
        if lastMove == "up":
            self.const = pygame.transform.rotate(self.bitmap, 0)
            self.y -= self.speed
        elif lastMove == "down":
            self.const = pygame.transform.rotate(self.bitmap, 180)
            self.y += self.speed
        elif lastMove == "left":
            self.const = pygame.transform.rotate(self.bitmap, 90)
            self.x -= self.speed
        elif lastMove == "right":
            self.const = pygame.transform.rotate(self.bitmap, -90)
            self.x += self.speed
        return lastMove    
    
    def InfiniteTank1(self):
        if self.x > width:
            self.x = -32
        elif self.x < -32:
            self.x = width
        elif self.y > height:
            self.y = -32
        elif self.y < -32:
            self.y = height
class Tank2():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.speed = 2
        self.bitmap = pygame.image.load(filename)
        self.const = self.bitmap
    
    def drawTank2(self):
        screen.blit(self.const,(self.x, self.y))
        return self.x, self.y
    
    def movementTank2(self, lastMove1):
        if lastMove1 == "up":
            self.const = pygame.transform.rotate(self.bitmap, 0)
            self.y -= self.speed
        elif lastMove1 == "down":
            self.const = pygame.transform.rotate(self.bitmap, 180)
            self.y += self.speed
        elif lastMove1 == "left":
            self.const = pygame.transform.rotate(self.bitmap, 90)
            self.x -= self.speed
        elif lastMove1 == "right":
            self.const = pygame.transform.rotate(self.bitmap, -90)
            self.x += self.speed
        return lastMove1    
    
    def InfiniteTank2(self):
        if self.x > width:
            self.x = -32
        elif self.x < -32:
            self.x = width
        elif self.y > height:
            self.y = -32
        elif self.y < -32:
            self.y = height

class Snaryad1():
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8
    
    def move(self):
        if self.direction == "up":
            self.y -= self.vel
        elif self.direction == "down":
            self.y += self.vel
        elif self.direction == "left":
            self.x -= self.vel
        elif self.direction == "right":
            self.x += self.vel
    
    def leave(self):
        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            return True
        return False
    
    def draw(self, screen):
        self.move()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
class Snaryad2():
    def __init__(self, x, y, radius, color, direction2):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction2 = direction2
        self.vel = 8
    
    def move2(self):
        if self.direction2 == "up":
            self.y -= self.vel
        elif self.direction2 == "down":
            self.y += self.vel
        elif self.direction2 == "left":
            self.x -= self.vel
        elif self.direction2 == "right":
            self.x += self.vel
    
    def leave2(self):
        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            return True
        return False
    
    def draw2(self, screen):
        self.move2()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def Intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x2 + w2 >= x1 >= x2) and (y2 + h2 >= y1 >= y2):
        return True
    elif (x2 + w2 >= x1 + w1 >= x2) and (y2 + h2 >= y1 >= y2):
        return True
    elif (x2 + w2 >= x1 >= x2) and (y2 + h2 >= y1 + h1 >= y2):
        return True
    elif (x2 + w2 >= x1 + w1 >= x2) and (y2 + h2 >= y1 + h2 >= y2):
        return True
    else:
        return False

def pause():
    paused = True
    while paused:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Paused. Press enter to continue', 220, 240, 20)
        
        pressed = pygame.key.get_pressed()  
        if pressed[pygame.K_RETURN]:
           paused = False
        pygame.display.update()
        fps.tick(15)

def win(who):
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('WIN: ' + who, 240, 240, 30)
        pygame.display.update()
        fps.tick(15)

def GameOver():
    gameover = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Game Over', 240, 240, 30)
        pygame.display.update()
        fps.tick(15)



def print_text(message, x, y, font_size, font_color = (0, 0, 0), font_type = None):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    window.blit(text, (x, y))

def drawWindow():
    tank1.InfiniteTank1()
    tank2.InfiniteTank2()

    screen.blit(bg, (0,0))
    
    tank1.drawTank1()
    tank2.drawTank2()
    
    for bullet in bullets:
        bullet.draw(screen)
    for bullet2 in bullets2:
        bullet2.draw2(screen)
    
    window.blit(screen, (0, 0))
    
    print_text('Hp1:= ' + str(Hp1), 10, 10, 25)
    print_text('Hp2:= ' + str(Hp2), 560, 10, 25)
    
    if Intersect(tank1.x, tank1.y, 30, 30, tank2.x, tank2.y, 30, 30) == True:
        Gameover_sound.play()
        GameOver()

    if Hp1 == 0:
        win('Player 1')
        Gameover_sound.play()
        GameOver()
    elif Hp2 == 0:
        win('Player 2')
        Gameover_sound.play()
        GameOver()
    
    pygame.display.flip()

def single():
    global tank1,tank2,Hp1,Hp2,bullets,bullets2
    tank1 = Tank1(100, height/2, 'tank1_up.png')
    tank2 = Tank2(500, height/2, 'tank2_up.png')

    lastMove = "stop"
    lastMove1 = "stop"

    bullets = []
    bullets2 = []

    Hp1 = 3
    Hp2 = 3
    done = True
    while done:
        fps.tick(30)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                        effect.play()
                        lastMove = "left"
                if e.key == pygame.K_RIGHT:
                        effect.play()
                        lastMove = "right"
                if e.key == pygame.K_UP:
                        effect.play()
                        lastMove = "up"
                if e.key == pygame.K_DOWN:
                        effect.play()
                        lastMove = "down"

                if e.key == pygame.K_a:
                        effect.play()
                        lastMove1 = "left"
                if e.key == pygame.K_d:
                        effect.play()
                        lastMove1 = "right"
                if e.key == pygame.K_w:
                        effect.play()
                        lastMove1 = "up"
                if e.key == pygame.K_s:
                        effect.play()
                        lastMove1 = "down"
                
                if e.key == pygame.K_RETURN:
                    fire.play()
                    direction = lastMove
                    if len(bullets) < 10:
                        bullets.append(Snaryad1(round(tank1.x + 32 // 2), round(tank1.y + 32 // 2), 3, (255, 0, 0), direction ))
                if e.key == pygame.K_SPACE:
                    fire.play()
                    direction2 = lastMove1
                    if len(bullets2) < 10:
                        bullets2.append(Snaryad2(round(tank2.x + 32 // 2), round(tank2.y + 32 // 2), 3, (0, 0, 255), direction2 ))
                if e.key==pygame.K_ESCAPE:
                    game_intro()

        for bullet in bullets:
            if bullet.leave():
                bullets.remove(bullet)
            if Intersect(bullet.x, bullet.y, 5, 5, tank2.x, tank2.y, 30, 30) == True: 
                sound.play()
                bullets.remove(bullet)
                Hp1 -= 1

        for bullet2 in bullets2:
            if bullet2.leave2():
                bullets2.remove(bullet2)
            if Intersect(bullet2.x, bullet2.y, 5, 5, tank1.x, tank1.y, 30, 30) == True: 
                sound.play()
                bullets2.remove(bullet2)
                Hp2 -= 1    
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]: pause()
        tank1.movementTank1(lastMove)
        tank2.movementTank2(lastMove1)
        drawWindow()

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
 
def button(txt,x,y,width,height,color,hover,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, hover,(x,y,width,height))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, color,(x,y,width,height))
    smallText = pygame.font.SysFont(None,26)
    textSurf, textRect = text_objects(txt, smallText)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    screen.blit(textSurf, textRect)


def game_intro():

    img=pygame.image.load("battle.jpg")
    intro = True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(img,(0,0))
        
        smallText = pygame.font.Font(None,40)
        button("Single Player Mode",250,170,300,50,(255,255,255),(255,255,255),single)
        pygame.display.update()
        pygame.display.flip()


game_intro()
        
