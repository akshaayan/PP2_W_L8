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
        self.image = Surface((100, 100))
        self.rect = Rect(200, 200, 20, 20) 
        # self.image.get_rect()
    
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
    
        
c1 = Car()
s1 = Square()
b1= Banner()

while True:
    e = event.wait()
    if e.type == QUIT:
        quit()
        
    keys_down = key.get_pressed()
    if keys_down[K_LEFT]:
        b1.update_l()
    elif keys_down[K_RIGHT]:
        b1.update_r()
    
    b1.update_r()
    # screen.blit(s1.image, s1.rect)
    # s1.image.fill((150, 30, 50))
    screen.fill((255, 255, 255))
    # screen.blit(c1.image, c1.rect)
    screen.blit(b1.image, b1.rect)
    
    

    display.update()
    clock.tick(100)