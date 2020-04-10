import math
import random
import pygame
from constants import *
import levels
import platforms


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet. """

    def __init__(self, start_x, start_y, dest_x, dest_y, arm):
        super().__init__()

        # Set up the image for the bullet
        spearpic = SPEAR

        spear = pygame.image.load(spearpic)

        pos = pygame.mouse.get_pos()

        angle = 360 - math.atan2(pos[1] - 300, pos[0] - 400) * 180 / math.pi

        pygame.transform.rotate(spear, angle)

        self.image = pygame.transform.rotate(spear, angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.start_x = start_x
        self.start_y = start_y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.arm_x, self.arm_y = arm.rect.x, arm.rect.y

        # Move the bullet to our starting location 
        self.rect.x = start_x
        self.rect.y = start_y


        # Because rect.x and rect.y are automatically converted 
        # to integers, we need to create different variables that 
        # store the location as floating point numbers. Integers 
        # are not accurate enough for aiming. 
        if self.dest_y > 400:
            self.floating_point_x = self.arm_x + 125
            self.floating_point_y = self.arm_y + 140
        elif self.dest_y < 200:
            self.floating_point_x = self.arm_x + 150
            self.floating_point_y = self.arm_y + 40
        else:
            self.floating_point_x = self.arm_x + 150
            self.floating_point_y = self.arm_y + 80

        # Calculation the angle in radians between the start points 
        # and end points. This is the angle the bullet will travel. 
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);

        # Taking into account the angle, calculate our change_x 
        # and change_y. Velocity is how fast the bullet travels. 
        velocity = 10
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

    def update(self):
        """ Move the bullet. """

        # The floating point x and y hold our more accurate location. 
        if self.dest_x > self.start_x + 5:
            self.floating_point_y += self.change_y
            self.floating_point_x += self.change_x

            # The rect.x and rect.y are converted to integers. 
            self.rect.y = int(self.floating_point_y)
            self.rect.x = int(self.floating_point_x)

            # If the bullet flies of the screen, get rid of it. 
            if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
                self.kill()
        else:
            self.kill()
    def collision(self):
    	pass