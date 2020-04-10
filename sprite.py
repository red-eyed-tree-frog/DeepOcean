"""

"""
import pygame

class SpriteOnScreen(pygame.sprite.Sprite):

    def __init__(self, sprite, x, y):
        super().__init__()
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        pass   