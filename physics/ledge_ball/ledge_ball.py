import pygame

pygame.init()

height = 800
width = 1000

window = pygame.display.set_mode((width, height))
bg = pygame.image.load('sky.jpg')
ledge = pygame.image.load('long.png')
playerImg = pygame.image.load('puffy.png')

class PLAYER:
    def __init__(self, x_pos, y_pos, x_speed, y_speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.image = pygame.transform.scale(playerImg, (110,110))

    
    def roll(self, angle):
        rotate_playerImg = pygame.transform.rotate(self.image, angle)
        rotation_rect = rotate_playerImg.get_rect(center=(self.x_pos + 55, self.y_pos + 55))
        window.blit(rotate_playerImg, rotation_rect.topleft)


class LEDGE:
    def __init__(self, scale, angle, x_pos, y_pos):
        self.scale = scale
        self.angle = angle
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        trans_ledge = pygame.transform.rotozoom(ledge, self.angle, self.scale)
        window.blit(trans_ledge, (self.x_pos, self.y_pos))

#music
music = pygame.mixer.music.load('ledgeballmusic.wav')
pygame.mixer.music.play(-1)
    

#game variables
ledge1 = LEDGE( 0.5, -90, 10, 400)
ledge2 = LEDGE(0.5, -90, 450, 600)
puffy = PLAYER(50, 300, 0, 0)
angle = 0
x_pos_change = 0
y_pos_change = 0
angle_change = 0

#main game loop
running = True
while running:
    window.blit(bg, (0,0))
    ledge1.draw()
    ledge2.draw()
    
  #  puffy.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x_pos_change = 2.5 
                angle_change = -2.5                
                
            if event.key == pygame.K_a:
                x_pos_change = -2.5
                angle_change = 2.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                x_pos_change = 0
                angle_change = 0

            if event.key == pygame.K_a:
                x_pos_change = 0
                angle_change = 0


    if puffy.x_pos > 475 and puffy.y_pos == 300: #fall off the first log
        y_pos_change = 4
    if puffy.y_pos ==  500:
        y_pos_change = 0

       
    if puffy.x_pos < 380 and puffy.y_pos == 500:  # fall off the second log
        y_pos_change = 4



    puffy.y_pos += y_pos_change
    angle += angle_change
    puffy.x_pos += x_pos_change        
    puffy.roll(angle)
    pygame.display.update()
