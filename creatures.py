"""
This module creates the random fish
"""
import pygame
import random
from constants import *

class Creatures(pygame.sprite.Sprite):

    def __init__(self, sprite, level):
        super().__init__()

        self.image = pygame.image.load(sprite).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.level = level
        self.diver_x = self.level.diver_x
        self.change_x = 0.05
        self.change_y = random.randint(1,2)
        self.amplitude =  random.randint(50, 150)
        self.rect.x = random.randint(1000, 15000) + self.diver_x
        self.startpoint = random.randint(150, 350)
        self.rect.y = self.startpoint
        self.oxygen = (-5.0)

    def update(self):
        self.rect.x -= self.change_x
        self.rect.y -= self.change_y
        if self.rect.y <= self.startpoint - self.amplitude or self.rect.y >= self.startpoint + self.amplitude:
            self.change_y = self.change_y * (-1.0)
    
        if self.rect.x + 200 <= 0:
            self.kill()
            cr = Creatures(CREATURES[random.randint(0, len(CREATURES)-1)], self.level)
            self.level.enemy_list.add(cr) #when killed adds new creatures (regeneration)

    def collision(self):
        self.level.player.oxygen_level(self.oxygen)
        # So no collision is detected
        self.mask = pygame.mask.from_surface(pygame.image.load(EMPTY).convert_alpha())
