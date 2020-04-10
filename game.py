import pygame
import time
from constants import *
from sprite import SpriteOnScreen
import platform_scroller
import os, sys

class Option:

    hovered = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((1280, 600))
pygame.display.set_caption('Welcome to Deep Ocean')

def pointer (x,y):

    x = (SCREEN_WIDTH * 0.45)
    y = (SCREEN_HEIGHT * 0.8)

pygame.mixer.music.load(RISE)
pygame.mixer.music.play(0)
time.sleep(5)
pygame.mixer.music.load(UTS)
pygame.mixer.music.play(-1)

while True:

    img = pygame.image.load(COVER)
    title = pygame.image.load(DEEP_OCEAN)
    exit = pygame.image.load(MENU[0])
    start = pygame.image.load(MENU[1])
    screen.blit(img, (0, 0))
    screen.blit(title, (0, 0))
    start_var = screen.blit(start, (550, 450))
    exit_var = screen.blit(exit, (800, 456))

    pointerImg = pygame.image.load(SUBMARINE).convert_alpha()
    pointerImg_rect = pointerImg.get_rect()
    pointerImg_rect.center = pygame.mouse.get_pos()
    screen.blit(pointerImg, pointerImg_rect)
    pygame.event.pump()
    done = False


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  
            if done:
                pygame.quit()
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_var.collidepoint(pygame.mouse.get_pos()):
                os.startfile(os.path.join(os.getcwd(), MAIN))
                sys.exit()
        
            if exit_var.collidepoint(pygame.mouse.get_pos()):
                sys.exit()

    pygame.display.update()
    
