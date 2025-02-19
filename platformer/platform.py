import pygame
import random

pygame.init()

WIDTH = 700
HEIGHT = 1000


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diddle Jump")
#load image
bg = pygame.image.load('bg.png').convert_alpha()
diddyImg = pygame.image.load('diddy.png').convert_alpha()
platformImg = pygame.image.load('platform.png').convert_alpha()

#set frame rate
clock = pygame.time.Clock()
FPS = 60


#game variables
WHITE = (255,255,255)
GRAVITY = 1
MAX_PLATFORMS = 10 
SCROLL_THRES = 500
scroll = 0 #controlls scrollling
bg_scroll = 0

#function fro drawinng infinite background
def draw_bg(bg_scroll):
    window.blit(bg, (0,0 + bg_scroll))
    window.blit(bg, (0, -1000 + bg_scroll))



#player class
class player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(diddyImg, (80,80))
        self.width = 30
        self.height = 130
        self.vel_y = 0
        self.rect = pygame.Rect(0,0, self.width , self.height - 46) #creating rectangle manually
        self.rect.center = (x,y)

    def draw(self):
        window.blit(self.image, (self.rect.x - 27, self.rect.y))#we are drawing image in the position of the rectangle
        pygame.draw.rect(window, WHITE, self.rect, 2) # it shows the rect wiht border ot 2 in white

    def move(self):
        #reset varriables
        dx = 0
        dy = 0
        scroll = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            dx = 10
        if key[pygame.K_a]:
            dx = -10
        #if key[pygame.K_w]:
         #   dy = -10
        #if key[pygame.K_s]:
         #   dy = 10

        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #update position    
        self.rect.x += dx
        self.rect.y += dy + scroll

        #border movements  
        if self.rect.right < 0:
            self.rect.x = 700
        if self.rect.left > 700:
            self.rect.x = -35

        #check collision wiht platform
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #checking above
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:  #if diidy is above then when its coming down, on colliison it jumps
                        self.rect.bottom = platform.rect.top 
                        dy  = 0
                        self.vel_y = -20

        #check collision with graond
        if self.rect.bottom >= HEIGHT:
            dy = 0
            self.vel_y = -21
        

        #check if diddy crossed scroll threshold
        if self.rect.top <= SCROLL_THRES:
            if self.vel_y < 0:

                scroll = -dy  #if player moves up by dy eeverthing moves down by dy
        
        return scroll    

#platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self) #initialize parent calss pygame.sprite.Sprite makes sure base sprite class is proerply setup before adding extra functionality
        self.image = pygame.transform.scale(platformImg, (width,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        # update platform y position
        self.rect.y += scroll

        if self.rect.top > HEIGHT:
            self.kill()  #kills insatances and those 10 instances keep repeating

#player calss isntance
diddy = player(WIDTH // 2 , (HEIGHT // 2) +200)
#create sprite gorups
platform_group = pygame.sprite.Group()

#create first  platforms
platform =  Platform(WIDTH // 2 -300, HEIGHT - 200, 130)
platform_group.add(platform)



run = True
while run:
    clock.tick(FPS)
    scroll = diddy.move()
    bg_scroll += scroll
    if bg_scroll >= 1000:
        bg_scroll = 0
    draw_bg(bg_scroll)
    #draw temporaru threshold
   # pygame.draw.line(window, WHITE, (0, SCROLL_THRES), (WIDTH, SCROLL_THRES))

    #generate platforms
    if len(platform_group) < MAX_PLATFORMS:
        p_w = random.randint(120, 130)
        p_x = random.randint(0, WIDTH - p_w)
        p_y = platform.rect.y - random.randint(150,200) # references platform before
        platform = Platform(p_x, p_y, p_w)
        platform_group.add(platform)
    platform_group.update(scroll)

    platform_group.draw(window) #auto draw method in the sprite class
    diddy.draw()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()        

