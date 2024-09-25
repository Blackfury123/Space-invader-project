import math
import pygame
import random

# constants
SCREEN_WIDTH=600
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=300
ENEMY_START_Y_MINIMUM=50
ENEMY_START_Y_MAXIMUM=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=20

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
caption=pygame.display.set_caption("SPACE INVADER")

background=pygame.image.load("background.png")

icon=pygame.image.load("ufo.png")

pygame.display.set_icon(icon)

player=pygame.image.load("player.png")
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0

enemy_img=[]
enemy_X=[]
enemy_Y=[]
enemyX_change=[]
enemyY_change=[]
number_of_enemy=16
