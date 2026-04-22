from pygame import *
from pygame.sprite import *
# from pygame.sprite import _Group
from pygame.font import Font

init()
screen = display.set_mode((400, 600))
display.set_caption("Net game")
my_font = Font(None, 50)
clock = time.Clock()

class Square(Sprite):
    def __init__(self):
        self.image = Surface((20, 20)).convert_alpha()
        self.rect = Rect(200, 200, 20, 20) 
        # self.image.get_rect()
    
    def update(self):
        self.rect.move(10, 0)
    
class Car(Sprite):
    def __init__(self):
        self.image = image.load(r'Lecture notes\YGpOh.png').convert_alpha()
        self.rect = self.image.get_rect().move(0, 0)
        
class Banner(Sprite):
    def __init__(self):
        self.image = my_font.render("New game text", True, (120, 35, 120), (200, 200, 255))
        self.rect = self.image.get_rect().move(40, 550)
        
    def update_l(self):
        self.rect = self.rect.move(-3, 0)
    
    def update_r(self):
        self.rect = self.rect.move(3, 0)
    

# drawn_rect = draw.circle(screen, (128, 0, 128), (120, 200), 30, 0)
        
c1 = Car()
s1 = Square()
b1= Banner()
direction = True

while True:
    e = event.get()
    for e in event.get(): 
        if e.type == QUIT:
            quit()
            break
        
        
    
    
    # screen.blit()
     
    # keys_down = key.get_pressed()
    # if keys_down[K_LEFT]:
    #     b1.update_l()
    # elif keys_down[K_RIGHT]:
    #     b1.update_r()
    
    # b1.update_r()
    # 
    
    
    screen.fill((255, 255, 255))
    
    # s1.rect.move(100, 0)
    s1.image.fill((128, 0, 128, 30))
    # s1.rect.move(x, 0)
    
    # s1.rect.x+=5
    if s1.rect.right >= 400 and direction:
        print(s1.rect.x)
        direction = False
        s1.rect.x-=5
        print('after: ', s1.rect.x)
    elif s1.rect.left <= 0 and not direction:
        direction = True
        s1.rect.x+=5
    elif direction:
        s1.rect.x+=5
    else:
        s1.rect.x-=5
    
    screen.blit(s1.image, s1.rect)
    # draw.circle(screen, (128, 0, 128), (120, 200), 30, 0)
    # draw.line(screen, (128, 0, 128), (10, 10), (10, 500), 300)
    # draw.polygon(screen, (210, 210, 100), ((10, 50), (65, 10), (120, 200), (300, 25), (150, 200)))
    # s1.rect.move(3, 0)
    
    
    # screen.blit(c1.image, c1.rect)
    # screen.blit(b1.image, b1.rect)

    display.update()
    clock.tick(10)