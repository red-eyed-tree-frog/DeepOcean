"""
This module creates the healthbar
"""
import pygame
import constants
class HealthBar(pygame.sprite.Sprite):

    def __init__(self, surf, percent):
        super().__init__()

        self.surf = surf
        self.percent = percent
        x = 69
        y = 560
        WHITE=(255,255,255)
        blue=(46,186,201)
        bar_length = -28
        bar_height = -69

        fill = float(self.percent/90) * bar_length
        bar_outline = pygame.Rect(x, y, bar_length, bar_height)
        bar_filled = pygame.Rect(x, y, bar_length, fill)
        pygame.draw.rect(self.surf, blue, bar_filled)
        pygame.draw.rect(self.surf, WHITE, bar_outline, 2)


    def update(self):
        pass


    '''Change quit to end game -> menu screen?'''