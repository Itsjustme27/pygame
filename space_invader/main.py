import pygame
import sys
import math
import random

pygame.init()

#Title odf window
pygame.display.set_caption("Space PewPew")

window = pygame.display.set_mode((1000,800))

#Player
playerImg = pygame.image.load('ship.png')
playerX = 460
playerY = 650
playerImg = pygame.transform.scale(playerImg, (80,80))
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('eyebot.png')
enemyX = 460
enemyY = 50
enemyImg = pygame.transform.scale(enemyImg, (90,90))
enemyX_change = 0.5


bulletImg = pygame.image.load("bullet.png")
bulletImg = pygame.transform.scale(bulletImg, (50,50))
bulletY_change = 0
bulletY = playerY
bulletX = playerX
bullet_state = "ready"

background = pygame.image.load('space.jpg')

#score
score_font = pygame.font.SysFont("Barron", 30)
score =0

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Barron.ttf", size)



def main_menu():
    pygame.display.set_caption("Menu")
    menuImg = pygame.image.load('moon.jpg')
    window.blit(menuImg, (0,0))
    while True:

        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run()

        pygame.display.update()



def draw_score(score, font, text_col, x, y):
    img = font.render(f"score: {score}", True, text_col)
    window.blit(img, (x, y) )


def player(x,y):
    window.blit(playerImg, (x,y))  #blit means to draw

def enemy(x,y):
    window.blit(enemyImg, (x,y))

def bullet(x, y):
    window.blit(bulletImg, (x+14, y))

def collision(x1, y1, x2, y2): #enemy cord and bullet cord
    distance = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    if distance <=40:
        return True
    else:
        return False

#game loop
run = True 
while run:
    window.fill((2, 64, 71))
    window.blit(background, (0,0))    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            run = False

        #userinput to manipulate movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.7


            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.7

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -0.7

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:

                playerY_change = 0.7

            if event.key == pygame.K_SPACE:
                bullet_state = "fire"
                bulletY = playerY
                bulletY_change = -1

        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0




    #make sure the ship doesn't go beyond boundary
    if playerX <=0:
        playerX =  900
    if playerX >= 925:
        playerX = 0
    if playerY <= 400:
        playerY = 400
    if playerY >= 700:
        playerY = 700

    #to make enemy move
    if enemyX >= 900:
        enemyX_change = -0.5
        enemyY = random.randint(0, 300)
    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY = random.randint(0, 300)



    enemyX += enemyX_change
    playerY += playerY_change
    playerX += playerX_change 
    bulletY += bulletY_change
    bulletX= playerX

    if bullet_state == "fire":
        bullet(bulletX, bulletY)



    player(playerX, playerY) # drawn only after fill so as to be on top of screen
    enemy(enemyX, enemyY) 

    #for collision
    bang = collision(enemyX, enemyY, bulletX, bulletY)
    if bang:
        bullet_state = "ready"
        enemyX = random.randint(0, 900)
        enemyY = random.randint(0, 400)
        score+=1

    draw_score(score, score_font, (255,255,255), 850, 750)



    pygame.display.update()

