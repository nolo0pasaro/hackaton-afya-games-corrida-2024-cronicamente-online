import pygame as pg, sys
from pygame.locals import QUIT

#Janela
width, height = 600, 1200
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Plataformer")  #Título da janela

#Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 250, 255)

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((32, 32))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.gravity = 0.35
        self.in_air = False
    

    def changespeed(self, x, y):
        self.change_x += x
        if y < 0:
            self.in_air = True
            self.change_y += y

    
    def apply_gravity(self):
        if self.in_air:
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += self.gravity
        

    def update(self):
        self.apply_gravity()
        self.rect.x += self.change_x
        
 
        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        self.rect.y += self.change_y
        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
        if len(block_hit_list) > 0 or self.rect.bottom >= height:
            self.change_y = 0
 


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
 
        self.image = pg.Surface([width, height])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


pg.init()
all_sprite_list = pg.sprite.Group()
wall_list = pg.sprite.Group()
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, height-10, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(width-10, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 600, 600, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 200, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(300, 500, 200, 50)
wall_list.add(wall)
all_sprite_list.add(wall)


player = Player(50, 50)
player.walls = wall_list

all_sprite_list.add(player)

clock = pg.time.Clock()

gameActive = True

while gameActive:
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
 
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.changespeed(-5, 0)
            elif event.key == pg.K_RIGHT:
                player.changespeed(5, 0)
            elif event.key == pg.K_UP:
                player.changespeed(0, -20)
 
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.changespeed(5, 0)
            elif event.key == pg.K_RIGHT:
                player.changespeed(-5, 0)
            elif event.key == pg.K_UP:
                player.changespeed(0, 20)

            

    player.apply_gravity()
    all_sprite_list.update()
    screen.fill(BLACK)
    all_sprite_list.draw(screen)
    pg.display.flip()
    clock.tick(60)
    print(player.change_y)

pg.quit()