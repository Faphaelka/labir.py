from typing import Any
from pygame import *

import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect = Rect(x, y, width, height)
        self.speed = speed

    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):
        change_x = 0
        change_y = 0
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            change_x = -self.speed
        if keys[K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            change_x = self.speed
        if keys[K_UP] and self.rect.y > 0:
            change_y = -self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - self.rect.height :
            change_y = self.speed
        self.rect.x += change_x
        self.rect.y += change_y
        if sprite.spritecollide(self, walls, False):
            self.rect.x -= change_x
            self.rect.y -= change_y


        
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 380:
            self.direction = 1
        if self.rect.x >= 900:
            self.direction = -1
        self.rect.x += self.speed * self.direction

WIDTH, HEIGHT = 1000, 600
window= display.set_mode((WIDTH, HEIGHT))
display.set_caption('лабірит')
background = transform.scale(image.load(resource_path('background.png')), (WIDTH, HEIGHT))
timer = time.Clock()

player = Player(resource_path('sprite1.png'), 10, 100, 80, 80, 7)
anemy = Enemy(resource_path('AngryBirds.png'), 380, 350, 100, 100, 7)
treasure = GameSprite(resource_path('sprite2.png'), 880, 500, 70, 70, 8)

walls = sprite.Group()
wall = GameSprite(resource_path('wall.jpg'), 145, 0, 20, 500, 0)
walls.add(wall)
wall = GameSprite(resource_path('wall.jpg'), 285, 100, 20, 600, 0)
walls.add(wall)
wall = GameSprite(resource_path('wall.jpg'), 425, 0, 20, 500, 0)
walls.add(wall)
wall = GameSprite(resource_path('wall.jpg'), 565, 100, 20, 600, 0)
walls.add(wall)
wall = GameSprite(resource_path('wall.jpg'), 705, 0, 20, 500, 0)
walls.add(wall)
wall = GameSprite(resource_path('wall.jpg'), 835, 100, 20, 600, 0)
walls.add(wall)

mixer.init()
mixer.music.load(resource_path('tree.mp3')) # mp3\ogg
mixer_music.play(-1)

font.init()
text_font = font.SysFont('chiller', 70)
game_over = text_font.render('', True, (230, 170, 130))
hint_font = font.SysFont('trebuchet ms', 30)
hint_text = hint_font.render('"SPACE" - resrart', True, (230, 230, 230))

game = True
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit(0)
    if game:
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        anemy.reset()
        anemy.update()
        treasure.reset()
        walls.draw(window)
        if sprite.collide_rect(player, treasure):
            game_over = text_font.render('Good job', True, (255, 50, 50))
            mixer.music.stop()
            game = False
        if sprite.collide_rect(player, anemy):
            game_over = text_font.render('Game over', True, (255, 50, 50))
            mixer.music.stop()
            game = False
    else:
        window.blit(game_over, (400, 250))
        window.blit(hint_text,(390, 320))
        keys = key.get_pressed()
        if keys[K_SPACE]:
            game = True
            player.rect.x = 10
            player.rect.y = 100

    display.update()
    timer.tick(60)
