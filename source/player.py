import pygame as pg
from pygame.key import get_pressed as gp

class Player():
    def __init__(self, x= 0, y = 0, w = 50, h = 50):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self):
        if gp()['K_a']:
            self.x -= 10
        if gp()['K_d']:
            self.x += 10
        if gp()['K_w']:
            self.y -= 10
        if gp()['K_s']:
            self.y == 10
    
    def draw(self):
        pg.draw.rect()