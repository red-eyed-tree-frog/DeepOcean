"""
This module creates the shark
"""
import pygame
import random
import constants

class Shark(pygame.sprite.Sprite):

    def __init__(self, sprite, level):
        super().__init__()

        self.image = pygame.image.load(sprite).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.change_x = 5
        self.change_y = random.randint(1,2) #should be lower, but then the bouncing doesn't work due to float numbers....
        self.amplitude = random.randint(50, 150)
        self.rect.x = random.randint(1000, 8000)
        self.startpoint = random.randint(200, 300)
        self.rect.y = self.startpoint
        self.level = level
        self.oxygen = (-5.0)
        self.attack = pygame.mixer.Sound('Sounds/shark_attack.wav')
        self.attack.set_volume(0.1)

    def update(self):
        self.rect.x -= self.change_x
        self.rect.y -= self.change_y
        if self.rect.y <= self.startpoint - self.amplitude or self.rect.y >= self.startpoint + self.amplitude :
            self.change_y = self.change_y * (-1.0)
    
        if self.rect.x + 150 <= 0:
            self.kill()
            sr = Shark(constants.SHARK[0], self.level)
            self.level.enemy_list.add(sr)

    def collision(self):
        self.level.player.oxygen_level(self.oxygen)
        #going to change
        self.attack.play()
