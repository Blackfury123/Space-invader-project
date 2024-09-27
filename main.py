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

player_img=pygame.image.load("player.png")
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0

enemy_img=[]
enemy_X=[]
enemy_Y=[]
enemyX_change=[]
enemyY_change=[]
number_of_enemy=16

for i in range(0,number_of_enemy):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_X.append(random.randint(0,SCREEN_WIDTH))
    enemy_Y.append(random.randint(ENEMY_START_Y_MINIMUM,ENEMY_START_Y_MAXIMUM))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyX_change.append(ENEMY_SPEED_Y)

bullet_img=pygame.image.load("bullet.png")
bullet_X=0
bullet_Y=PLAYER_START_Y
bullet_x_change=0
bullet_y_change=BULLET_SPEED_Y

score=0
font = pygame.font.Font('freesansbold.ttf', 32)
textx=10
texty=10

over_font=pygame.font.Font('freesansbold.ttf',75)

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over():
    gameOver=font.render("GAME OVER",True,(255,255,255))
    screen.blit(gameOver,(200, 250))

def enemy(x, y , i ):
    screen.blit(enemy_img[i],(x, y))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE
    
def player(x,y):
    screen.blit(player_img,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x,y))

running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerX_change = -5
          if event.key == pygame.K_RIGHT:
              playerX_change = 5
          if event.key==pygame.K_SPACE and bullet_state=="ready":
              bullet_X=playerX
              fire_bullet(bullet_X,bullet_Y)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerX_change=0