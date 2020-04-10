"""
This module creates the random fish
"""
import pygame
import random
from constants import *

class Bubbles(pygame.sprite.Sprite):

    def __init__(self, level):
        super().__init__()

        self.level = level
        self.size = random.randint(1, 3)
        self.image = pygame.image.load(BUBBLES[self.size - 1]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.change_y = random.randint(1,2)
        self.diver_x = self.level.diver_x
        self.startpoint = random.randint(1500, 10000) + self.diver_x
        self.rect.x = self.startpoint 
        self.rect.y = random.randint(100, SCREEN_WIDTH)
        self.amplitude = random.randint(30, 50)
        self.bubsound = pygame.mixer.Sound(BUBBLE)

        if self.size == 1:
            self.oxygen = 10
        elif self.size == 2:
            self.oxygen = 7
        else:
            self.oxygen = 5

    def update(self):

        self.rect.y -= self.change_y
        if self.rect.y + 100 <= 0:
            self.rect.y = 600

    def collision(self):
        
        self.level.player.oxygen_level(self.oxygen)
        self.pop()
        self.bubsound.play()
        

    def pop(self):
        self.image = pygame.image.load(BUBBLES_POP[self.size - 1]).convert_alpha()
        self.mask = pygame.mask.from_surface(pygame.image.load(EMPTY).convert_alpha())