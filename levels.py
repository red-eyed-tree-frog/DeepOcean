import pygame
import constants
import platforms
from treasury import Treasure
from creatures import Creatures
from shark import Shark
from bubble import Bubbles
import pygame, random
from sprite import SpriteOnScreen

class Level():

    def __init__(self, player, level, background, platform, creatures_list, shark_list, bubble_number, shell_number, diver_x):
        # Lists of sprites used in all levels. 
        self.platform_list = None
        self.treasure_list = None
        self.enemy_list = None
        self.shark_list = None
        # Background 
        self.background = None
        # How far world has been scrolled right
        self.world_shift = 0
        self.platform_list = pygame.sprite.Group()
        self.treasure_list = pygame.sprite.Group()
        self.bubbles_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.shark_list = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.level = level
        self.player = player
        self.background = pygame.image.load(background).convert()
        self.background.set_colorkey
        self.level_limit = -11500
        self.creature = creatures_list
        self.shark = shark_list
        self.diver_x = diver_x
        self.bubble_number = bubble_number
        self.shell_number = shell_number

        """
        looping through a list of variables to add items
        """
        for creature in self.creature:
            cr = Creatures(creature, self)
            self.enemy_list.add(cr)

        for shark in self.shark:
            sr = Shark(shark, self)
            self.enemy_list.add(sr)

        for treasure in range(self.shell_number):
            tr = Treasure(self)
            self.treasure_list.add(tr)

        for bubble in range(self.bubble_number):
            bu = Bubbles(self)
            self.bubbles_list.add(bu)

        self.floor.add(SpriteOnScreen(platform,0,0))

    # Update everything on this level
    def update(self):

        self.platform_list.update()
        self.floor.update()
        self.treasure_list.update()
        self.enemy_list.update()
        self.bubbles_list.update()
        self.shark_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.VIOLET)
        screen.blit(self.background, (0, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.floor.draw(screen)
        self.treasure_list.draw(screen)
        self.enemy_list.draw(screen)
        self.bubbles_list.draw(screen)
        self.shark_list.draw(screen)


    def shift_world(self, shift_x):

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for treasure in self.treasure_list:
            treasure.rect.x += shift_x 

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for bubble in self.bubbles_list:
            bubble.rect.x += shift_x

        for fl in self.floor:
            fl.rect.x += shift_x

    #collision detection for the player with a specific sprite list
    def collision_det(self, sprite_list):
        for item in sprite_list:
            offset = (self.player.rect.x - item.rect.x, self.player.rect.y - item.rect.y)
            result = item.mask.overlap(self.player.maskR, offset)

            if result:
                item.collision()
                # calls item method collision

    #collision detecion for two lists             
    def collision_det2(self, sprite_list1, sprite_list2):
        for sprite1 in sprite_list1:
            for sprite2 in sprite_list2:
                offset = (sprite1.rect.x - sprite2.rect.x, sprite1.rect.y - sprite2.rect.y)
                result = sprite2.mask.overlap(sprite1.mask, offset)

                if result:
                    sprite2.kill()