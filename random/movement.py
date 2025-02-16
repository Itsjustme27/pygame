import pygame
import random


pygame.init()

width = 1000
height = 800
 
window = pygame.display.set_mode((width, height))
bg_color = ['white', 'black']

class triangle:
    def __init__(self, color, x_speed, y_speed, x1, y1, x2, y2, x3, y3):
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self):
        pygame.draw.polygon(window, self.color, [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)])
        
    def update(self):
        # Move the triangle by updating its vertex positions
        self.x1 += self.x_speed
        self.y1 += self.y_speed
        self.x2 += self.x_speed
        self.y2 += self.y_speed
        self.x3 += self.x_speed
        self.y3 += self.y_speed

#game variables
color = "white"
triangle1 = triangle("white", 0, 0, 100,100,500,100,100,400)
triangle2 = triangle("black", 0, 0, 500,100,900,100,900,400)
triangle3 = triangle("black", 0, 0, 100,400,100,700,500,700)
triangle4 = triangle("white", 0, 0, 900,400,900,700,500,700)
triangle5 = triangle("white", 0, 0, 300,400,700,400,500,300)
triangle6 = triangle("black", 0, 0, 300,400,700,400,500,500)


#main loop
running = True
while running:
    window.fill((color))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = random.choice(bg_color)
            if event.key == pygame.K_d:
                triangle1.x_speed = 0.2
                triangle1.y_speed = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                triangle1.x_speed = 0
                triangle1.y_speed = 0

    triangle1.update()

    triangle1.draw()
    triangle2.draw()
    triangle3.draw()
    triangle4.draw()
    triangle5.draw()
    triangle6.draw()

    pygame.display.flip()

    pygame.display.update()


pygame.quit()




