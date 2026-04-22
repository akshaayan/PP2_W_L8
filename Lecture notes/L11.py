from pygame import * 
from snake_db import *
import random

init()
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
FPS = 8

snake = [(100, 100), (80, 100), (60, 100)]
f1 = font.Font(None, 32)
dx, dy = CELL, 0
score = 0
level = 1
foods_eaten = 0
walls = set()
game_active = True
food = False
input_box = Rect(210, 20, 250, 20)
color_inactive = Color('lightskyblue3')
color_active = Color('dodgerblue2')
color = color_inactive
active = False
text = ''

def game_over_screen(text):
    # Render the current text.
        txt_surface = f1.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        draw.rect(screen, color, input_box, 2)
   

def out_of_bounds(x, y):
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT

def random_free_cell():
        while True:
            cell = (random.randrange(0, WIDTH, CELL),
                    random.randrange(0, HEIGHT, CELL))
            if cell not in snake and cell not in walls:
                return cell

def create_food():
    return {
        "pos": random_free_cell(),
        "weight": random.choice([1, 2, 3]),
        "ttl_ms": random.choice([4000, 7000, 10000]),
        "spawn_time": time.get_ticks()
    }

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord[0] 
        y = coord[1]
        wormSegmentRect = Rect(x, y, CELL, CELL)
        draw.rect(screen, (0, 255, 0), wormSegmentRect)
        wormInnerSegmentRect = Rect(x + 4, y + 4, CELL - 8, CELL - 8)
        draw.rect(screen, (0, 255, 0), wormInnerSegmentRect)


def drawApple(coord):
    x = coord['pos'][0] 
    y = coord['pos'][1]
    appleRect = Rect(x, y, CELL, CELL)
    draw.rect(screen, (255, 0, 0), appleRect)



while game_active:
    for e in event.get():
        if e.type == QUIT:
            game_active= not game_active
        elif e.type == MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(e.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
        elif e.type == KEYDOWN:
            if e.key == K_UP and dy == 0:
                dx, dy = 0, -CELL
            elif e.key == K_DOWN and dy == 0:
                dx, dy = 0, CELL
            elif e.key == K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            elif e.key == K_RIGHT and dx == 0:
                dx, dy = CELL, 0
            
            if active:
                if e.key == K_RETURN:
                    print(text)
                    update_score((text, score, level, foods_eaten))
                    text = ''
                elif e.key == K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += e.unicode

    screen.fill((0, 0, 0))
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    
    # if out_of_bounds(*new_head) or new_head in walls:
    #     game_active = False

    

    if not food:
       food = create_food() 
    
    now = time.get_ticks()
    if now - food["spawn_time"] > food["ttl_ms"]:
        food = create_food()

    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    drawWorm(snake)
    drawApple(food)
    
    
    if new_head in snake[1:]:
        game_active = False
        game_over_screen(text)
    
    if out_of_bounds(*new_head) or new_head in walls or new_head in snake[1:]:
        game_over = True
        game_over_screen(text)
    else:
        snake.insert(0, new_head)
        if new_head == food["pos"]:
            foods_eaten += 1
            score += food["weight"]
            if foods_eaten % 4 == 0:
                level += 1
                FPS += 2
            food = create_food()
        else:
            snake.pop()
    
    # score += food["weight"]
    # food = random_free_cell()
    
    f = font.Font(None, 24)
    hud = f.render(f"Score: {score}   Level: {level}", True, (255, 255, 255))
    screen.blit(hud, (10, 10))
  
    
    display.flip()
    clock.tick(20)
    



