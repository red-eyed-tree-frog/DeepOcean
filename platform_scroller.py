import pygame
from constants import *
from levels import Level
from player import Player
from healthbar import HealthBar
import treasury
import creatures
import shark
from bullets import Bullet
from score import Score
from sprite import SpriteOnScreen
import time
from highscores import highscore
from arm import Arm

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
scoreboardfont = pygame.font.SysFont("Arial", 16)


def menu():
    pass

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def game_over(pearls):
    dothis = True
    clock = pygame.time.Clock()
    pygame.display.set_caption('Time to come up for air!')
    ovimg = pygame.image.load(SUNKEN)
    my_score = pearls


    while dothis:
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.K_SPACE:
                return main()
            elif event.type == pygame.QUIT:
                pygame.quit()
                time.sleep(30)
                quit()

        screen.blit(ovimg, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Game Over", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 1.4))
        screen.blit(TextSurf, TextRect)
        highscore(screen, 'score_file.txt', my_score)
        txt_surf = scoreboardfont.render("Shall we go down to the sea again...", True, BLACK)
        txt_rect = txt_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(txt_surf, txt_rect)

        pygame.display.update()
        clock.tick(15)

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen

    pygame.display.set_caption("Deep Ocean")
    pygame.mixer.music.load(YB)
    pygame.mixer.music.play(-1)
    # Create the player
    player = Player()

    bullet_list = pygame.sprite.Group()

    # Create all the levels
    level_list = []
    #                       player, level, background, creatures_list, shark_list, bubble_number, shell_number, diver_x
    level_list.append(Level(player, 1, BACK, PLATFORM, CREATURES, SHARK, 20, 20,  player.rect.x))
    level_list.append(Level(player, 2, BACK, PLATFORM, CREATURES, SHARK, 15, 15,  player.rect.x))
    level_list.append(Level(player, 3, BACK, PLATFORM, CREATURES, SHARK, 10, 10,  player.rect.x))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    arm = Arm(current_level)
    active_sprite_list.add(arm)
    # static images

    score_shell = SpriteOnScreen(SCORE_SHELL, 13, 16)
    tank = SpriteOnScreen(HEALTHBAR, 30, 450)
    score_number = Score(screen, current_level.player.pearls, current_level)
    active_sprite_list.add(score_shell, tank, score_number)

    # Loop until the user clicks the close button.
    done = False
    over = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    shot = pygame.mixer.Sound(SHOT)
    shot.set_volume(0.5)
    endsound = pygame.mixer.Sound(GAME_OVER)
    endsound.set_volume(0.1)

    # -------- Main Program Loop -----------

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                shot.play()

                # Get the mouse position
                pos = pygame.mouse.get_pos()

                mouse_x = pos[0]
                mouse_y = pos[1]

                # Create the bullet based on where we are, and where we want to go.
                bullet = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y, arm)

                # Add the bullet to the lists
                active_sprite_list.add(bullet)
                bullet_list.add(bullet)

            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LEFT:
                #     player.go_left()
                #     player.stop()
                #     player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_DOWN:
                    player.dive()

            if event.type == pygame.KEYUP:
                # if event.key == pygame.K_LEFT and player.change_x < 0:
                #     player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player.collect()


        current_level.collision_det(current_level.enemy_list)
        current_level.collision_det(current_level.treasure_list)
        current_level.collision_det(current_level.bubbles_list)
        current_level.collision_det2(bullet_list, current_level.enemy_list)

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        for bullet in bullet_list:

            # See if it hit a block
            # block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                active_sprite_list.remove(bullet)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        HealthBar(screen, current_level.player.oxygen)
        active_sprite_list.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(FPS)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        if current_level.player.oxygen < 20:
            endsound.play()

        if current_level.player.oxygen <= 0:
            over = True

        if over == True:
            return game_over(current_level.player.pearls)


    pygame.quit()

if __name__ == "__main__":
    main()
