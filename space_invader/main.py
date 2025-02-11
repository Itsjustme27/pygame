import pygame
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
    if distance <=30:
        return True
    else:
        return False

#game loop
running = True
while running:

    window.fill((2, 64, 71))
    window.blit(background, (0,0))    

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #userinput to manipulate movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5

            
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5 

            if event.key == pygame.K_UP:
                playerY_change = -0.5

            if event.key == pygame.K_DOWN:
               
                playerY_change = 0.5

            if event.key == pygame.K_SPACE:
                bullet_state = "fire"
                bulletY = playerY
                bulletY_change = -1

        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0



   
    #make sure the ship doesn't go beyond boundary
    if playerX <=0:
        playerX = 0
    if playerX >= 925:
        playerX = 925
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
