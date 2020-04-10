'''Treasure module'''
import pygame, random
from constants import *

class Treasure(pygame.sprite.Sprite):
    """ Treasure the player collects """
    def __init__(self, level):

        super().__init__()

        self.shell_number = random.randint(1, 3)
        self.image = pygame.image.load(SHELLS[self.shell_number - 1]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(800, BG_WIDTH)
        self.rect.y = random.randint(500, 550)
        self.coins = random.randint(1,5)
        self.level = level
        self.find = pygame.mixer.Sound(FIND)

    def update(self):
        pass

    def collision(self):
        self.image = pygame.image.load(OPEN_SHELLS[self.shell_number - 1]).convert_alpha()
        # Makes the mask transparent so the shell wouldn't disappear
        self.mask = pygame.mask.from_surface(pygame.image.load(EMPTY).convert_alpha())
        self.level.player.collect()
        self.find.play()