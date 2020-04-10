"""
Global constants
"""
import os
import pygame
# Colors
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
VIOLET = (75,0,130)
GOLD = (255,215,0)
# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 600
BG_WIDTH = 12000

# ALL PATHS TO SPRITES DOWN BELOW
# Making sure it works on all OS due to /\ 
vector_dir = 'game_vectors'
sounds = 'Sounds'

# Transparent empty image so collission would not be detected
EMPTY = os.path.join(vector_dir,'empty.png')

BACK = os.path.join(vector_dir,'BACK.png')
PLATFORM = os.path.join(vector_dir,'PLATFORM.png')

SOUND = [
     os.path.join(sounds,'shot.wav'),
     os.path.join(sounds,'oof.wav'),
     os.path.join(sounds,'bubblehi.wav'),
     os.path.join(sounds,'bubblelo.wav'),
     os.path.join(sounds,'rise.m3'),
     os.path.join(sounds,'water.mp3'),
     os.path.join(sounds, 'pings.wav')]

OVERBG = os.path.join('Ocean 08.png')

LEVEL1_bg = os.path.join(vector_dir, 'back800.png')
LEVEL2_bg = os.path.join(vector_dir, 'back800.png')

SPEAR = os.path.join(vector_dir, 'spearR1.png')

HEALTHBAR = os.path.join(vector_dir, 'healthbar.png')

SUNKEN = os.path.join(vector_dir,'sunken-ship.jpg')

MAIN = os.path.join('platform_scroller.py')
MAIN_MENU = os.path.join('game.py')

SHELLS = [
     os.path.join(vector_dir,'shell1.png'),
     os.path.join(vector_dir,'shell2.png'),
     os.path.join(vector_dir,'shell3.png')]

OPEN_SHELLS = [
     os.path.join(vector_dir,'shell11.png'),
     os.path.join(vector_dir,'shell22.png'),
     os.path.join(vector_dir,'shell33.png')]



BUBBLES = [
     os.path.join(vector_dir, 'bubble1.png'),
     os.path.join(vector_dir, 'bubble11.png'),
     os.path.join(vector_dir, 'bubble111.png')]

BUBBLES_POP = [
     os.path.join(vector_dir, 'bubble3.png'),
     os.path.join(vector_dir, 'bubble33.png'),
     os.path.join(vector_dir, 'bubble333.png')]

CREATURES = [
     os.path.join(vector_dir,'fish1.png'),
     os.path.join(vector_dir,'fish2.png'),
     os.path.join(vector_dir,'fish3.png'),
     os.path.join(vector_dir,'fish4.png'),
     os.path.join(vector_dir,'fish5.png'),
     os.path.join(vector_dir,'fish6.png'),
     os.path.join(vector_dir,'fish7.png'),
     os.path.join(vector_dir,'fish8.png'),
     os.path.join(vector_dir,'fish9.png'),
     os.path.join(vector_dir,'fish10.png'),
     os.path.join(vector_dir,'fish11.png'),
     os.path.join(vector_dir,'fish12.png'),
     os.path.join(vector_dir,'fish13.png'),
     os.path.join(vector_dir,'fish14.png')] *10

SHARK = [
     os.path.join(vector_dir, 'shark1.png')]

DIVER = [
     os.path.join(vector_dir, 'diver1.png'),
     os.path.join(vector_dir, 'diver2.png'),
     os.path.join(vector_dir, 'diver1left.png'),
     os.path.join(vector_dir, 'diver2left.png'),
     os.path.join(vector_dir, 'diver1arm.png'),
     os.path.join(vector_dir, 'diver2arm.png'),
     os.path.join(vector_dir, 'diver1leftarm.png'),
     os.path.join(vector_dir, 'diver2leftarm.png')]


MENU = [
     os.path.join(vector_dir, 'exit.png'),
     os.path.join(vector_dir, 'start.png'),
     os.path.join(vector_dir, 'highscores.png')]

COVER = os.path.join(vector_dir, 'cover2.jpg')
DEEP_OCEAN = os.path.join(vector_dir, 'deep_ocean.png')
SUBMARINE = os.path.join(vector_dir, 'subicon.png')

number_dir = 'numbers'

SCORE_SHELL = os.path.join(vector_dir, number_dir,'score_shell.png')

SCORE_NUMBER = [
     os.path.join(vector_dir, number_dir, 'zero.png'),
     os.path.join(vector_dir, number_dir, 'one.png'),
     os.path.join(vector_dir, number_dir, 'two.png'),
     os.path.join(vector_dir, number_dir, 'three.png'),
     os.path.join(vector_dir, number_dir, 'four.png'),
     os.path.join(vector_dir, number_dir, 'five.png'),
     os.path.join(vector_dir, number_dir, 'six.png'),
     os.path.join(vector_dir, number_dir, 'seven.png'),
     os.path.join(vector_dir, number_dir, 'eight.png'),
     os.path.join(vector_dir, number_dir, 'nine.png'),
     os.path.join(vector_dir, number_dir, 'ten.png'),
     os.path.join(vector_dir, number_dir, 'eleven.png'),
     os.path.join(vector_dir, number_dir, 'twelve.png'),
     os.path.join(vector_dir, number_dir, 'thirteen.png'),
     os.path.join(vector_dir, number_dir, 'fourteen.png'),
     os.path.join(vector_dir, number_dir, 'fiveteen.png'),
     os.path.join(vector_dir, number_dir, 'sixteen.png'),
     os.path.join(vector_dir, number_dir, 'seventeen.png'),
     os.path.join(vector_dir, number_dir, 'eighteen.png'),
     os.path.join(vector_dir, number_dir, 'nineteen.png'),
     os.path.join(vector_dir, number_dir, 'twenty.png'),
     os.path.join(vector_dir, number_dir, 'twentyone.png'),
     os.path.join(vector_dir, number_dir, 'twentytwo.png'),
     os.path.join(vector_dir, number_dir, 'twentythree.png'),
     os.path.join(vector_dir, number_dir, 'twentyfour.png'),
     os.path.join(vector_dir, number_dir, 'twentyfive.png'),
     os.path.join(vector_dir, number_dir, 'twentysix.png'),
     os.path.join(vector_dir, number_dir, 'twentyseven.png'),
     os.path.join(vector_dir, number_dir, 'twentyeight.png'),
     os.path.join(vector_dir, number_dir, 'twentynine.png'),
     os.path.join(vector_dir, number_dir, 'thirty.png')]


sound_dir = 'Sounds'

OOF = os.path.join(sound_dir, 'oof.wav')

UTS = os.path.join(sound_dir, 'uts.mp3')

YB = os.path.join(sound_dir, 'ys.mp3')

SHOT = os.path.join(sound_dir, 'shot1.wav')

GAME_OVER = os.path.join(sound_dir, 'gameoverquiet.wav')

RISE = os.path.join(sound_dir, 'rise.mp3')

FIND = os.path.join(sound_dir, 'find.wav')

BUBBLE = os.path.join(sound_dir, 'bubblehi.wav')