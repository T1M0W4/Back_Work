import pygame as pg

class Player():
    size = (0,0)
    position = (0,0)
    color = "green"
    sprite = None
    frame = 0
    surface: pg.Surface = None

def __init__(self, size, position, color):
    self.size = size
    self.position = position
    self.color = color
    self.sprite = pg.image.load('resources\GG_mage\mage-dark.png')
    self.surface = pg.Surface((self.size))
    update(self.surface)
    self.surface.set_colorkey((0, 0, 0))

def update(self):
    self.surface.fill((0, 0, 0))
    self.surface.blit(self.sprite, (0, 0), (self.size[0]*self.frame, 0, self.size[0]*(self.frame+1), self.size[1]))

def next_frame(self):
    self.frame += 1
    if self.frame > 11:
        self.frame = 0

def move(self, dx, dy):
    self.position = (self.position[0]+dx, self.position[1]+dy)
    next_frame()