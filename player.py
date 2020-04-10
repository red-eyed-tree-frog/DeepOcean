"""
Player class with movement control/attributes
"""
import pygame
import constants
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
import treasury
import levels
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
   controls. """
 
    # -- Methods
    def __init__(self):
 
        super().__init__()
 
        # -- Attributes
        # Set speed of player
        self.change_x = 3
        self.change_y = 0
 
        # This holds all the images for the player
        self.walking_frames_r = []
 
        # Oxygen level
        self.oxygen = 200.0

        # Pearls
        self.pearls = 0
 
        # List of sprites we can hit
        self.level = None
        self.state = "ready"
 
        # sprite_sheet = SpriteSheet(constants.DIVER)
        # Load all the right facing images 
        image = pygame.image.load(constants.DIVER[0]).convert_alpha()
        self.walking_frames_r.append(image)
        image = pygame.image.load(constants.DIVER[1]).convert_alpha()
        self.walking_frames_r.append(image)
 
        #Create masks for colission detection
        self.maskR = pygame.mask.from_surface(self.walking_frames_r[0])
 
        # Set the image the player starts with
        self.image = self.walking_frames_r[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
 
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
 
        if (self.rect.y + self.rect.height) > constants.SCREEN_HEIGHT:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - 1 - self.rect.height
 
        if self.rect.y <= 0:
            self.change_y = 0
            self.rect.y = 1
 
        frame = (pos // 40) % len(self.walking_frames_r)
        self.image = self.walking_frames_r[frame]

 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 10
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
 
        # Oxygen decreases with time
        self.oxygen -= 0.1

    def calc_grav(self):
        """ Calculate effect of gravity. """
        grav_constant = 0.0015
        self.change_y -= grav_constant * (self.rect.y - (constants.SCREEN_HEIGHT/1.75))
 
   
    def jump(self):
        """ Called when user hits 'jump' button. """
        if self.state == "jump":
            self.change_y -= 5
            self.state = "double-jump"
        else:
            self.change_y -= 13
            self.state = "jump"

        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)

        # If ok to jump, set speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT/2.5:
            self.change_y = -5
 
    def dive(self):
        """ Called when user hits 'down' key. """
        if self.state == "dive":
            self.change_y += 1
            self.state = "double-dive"
        else:
            self.change_y += 3
            self.state = "dive"

        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
 
        # If ok to jump, set speed upwards
        if len(platform_hit_list) > 0 or self.rect.top <= constants.SCREEN_HEIGHT / 2.5:
            self.change_y = 0
 
    # Player movement: 
    def go_right(self):
        self.change_x += 3
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 3

    def collect(self):
        
        self.pearls += 1

    def oxygen_level(self, number):

        self.oxygen = int(self.oxygen + number)