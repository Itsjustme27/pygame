import pygame

pygame.init()

height = 800
width = 1000
window = pygame.display.set_mode((width, height))
fps = 60
timer = pygame.time.Clock()


#game variable
gravity = 0.5
bounce_stop = 0.3
thickness = 30



class Ball:
    def __init__(self, x_pos, y_pos, radius, color, retention, x_speed, y_speed, mass, id):
        self.x_pos= x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention =retention
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.id = id
        self.circle = ' '

    def draw(self):
        self.circle = pygame.draw.circle(window, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self):
        if self.y_pos < height - self.radius - (thickness/2):
            self.y_speed += gravity
        else:
            if self.y_speed > bounce_stop:  #bounce if its value is greater than bounce stop
                self.y_speed = self.y_speed * -1 * self.retention  #keeps boouncing with chaning direction
            else:
                if abs(self.y_speed) <= bounce_stop:
                    self.y_speed = 0
        return self.y_speed            

    def update_pos(self):
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed


def draw_walls():
    left = pygame.draw.line(window, 'black', (0, 0), (0, height), thickness)  # last parameter is thickness
    right = pygame.draw.line(window, 'black', (width, 0), (width, height), thickness)
    top = pygame.draw.line(window, 'black', (0, 0), (width, 0), thickness)
    bottom = pygame.draw.line(window, 'black', (width, height), (0, height), thickness)
    wall_list= [left, right, top, bottom]
    return wall_list

ball1 = Ball(200, 200, 100, 'red', 0.5, 0, 0, 10, 1)
ball2 = Ball(500, 200, 60, 'green', 0.8, 0, 0, 100, 1)
ball3 = Ball(700, 520, 70, 'black', 0.9, 0, 0, 40, 1)



#main game loop
run = True
while run:

    timer.tick(fps)
    window.fill((240, 166, 70))
     
    ball1.draw() 
    ball2.draw()
    ball3.draw()

    ball1.update_pos()
    ball2.update_pos()
    ball3.update_pos()

    ball1.y_speed = ball1.check_gravity()
    ball2.y_speed = ball2.check_gravity()
    ball3.y_speed = ball3.check_gravity()
    walls = draw_walls()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()   
