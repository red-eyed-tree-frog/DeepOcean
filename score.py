"""
This module creates the score image
"""
import pygame
from constants import SCORE_NUMBER, SCORE_SHELL
class Score(pygame.sprite.Sprite):

    def __init__(self, surf, pearl_number, level):
        super().__init__()
        x = 130
        y = 33
        self.score = pearl_number
        self.image = pygame.image.load(SCORE_NUMBER[self.score]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = level

    def update(self):

        self.score = self.level.player.pearls
        self.image = pygame.image.load(SCORE_NUMBER[self.score]).convert_alpha()