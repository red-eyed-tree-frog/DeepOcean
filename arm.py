import pygame
from constants import *
import math

class Arm(pygame.sprite.Sprite):
    """ Arm class """
    def __init__(self, level):

        super().__init__()

        self.change_x = 3
        self.change_y = 0

        self.arm_right = []


        self.rightarm = pygame.image.load(DIVER[4]).convert_alpha()
        self.arm_right.append(self.rightarm)

        self.image = self.arm_right[0]
        self.rect = self.image.get_rect

        self.level = level

        self.malcomX = self.level.player.rect.x
        self.malcomY = self.level.player.rect.y


    def update(self):

        self.mpos = pygame.mouse.get_pos()
        self.angle = 360 - math.atan2(self.mpos[1] - 300, self.mpos[0] - 400) * 180 / math.pi
        self.arm_right[0] = pygame.transform.rotate(self.rightarm, self.angle)
        self.malcomX = self.level.player.rect.x
        self.malcomY = self.level.player.rect.y

        self.image = self.arm_right[0]
        self.rect = self.image.get_rect(center=(self.malcomX+110, self.malcomY+70))


    def collision(self):
        pass