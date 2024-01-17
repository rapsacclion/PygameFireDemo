import random, copy

import pygame
  
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

firelist = []
# define the RGB value
# for white colour
  
# assigning values to X and Y variable
X = 2400
Y = 1000
  
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))
  
# set the pygame window name
pygame.display.set_caption('Image')
  
# create a surface object, image is drawn on it.
image = pygame.image.load('floating_tank.png')
angle = 0
pos = [0, 0]
boom = False
# infinite loop
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


class fire:
    def __init__(self, pos):
        self.pos = pos
        colormarker = random.randint(100, 255)
        self.color = (colormarker, random.randint(20, colormarker-40), 0)
        
        self.size = random.randint(200, 500)
        if boom:
            self.size = random.randint(500, 800)
        firelist.append(self)
    def explosion(self):
        pygame.draw.rect(display_surface, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size/10, self.size/10))
        self.size -= random.randint(1, 12)
        self.pos = (self.pos[0]+random.randint(-25, 25), self.pos[1]+random.randint(-20, 5))
        if random.randint(0, 150) == 5:
            newfire = fire(self.pos)
        if self.size < 5:
            firelist.remove(self)
            del self
    def update(self):
        pygame.draw.rect(display_surface, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size/10, self.size/10))
        self.size -= random.randint(1, 6)
        self.pos = (self.pos[0]+random.randint(-1, 1), self.pos[1]+random.randint(-2, 0))
        if self.size < 5:
            firelist.remove(self)
            del self
rtime = 0

def explode():
    global boom
    if boom:
        firelist = []
    boom = not boom
while True :
    rtime += 1
    
    pastpos = pos
    pos = pygame.mouse.get_pos()
    
    speed = ((pastpos[0] - pos[0])+(pastpos[0] - pos[0]))/2
    angle += speed
    # completely fill the surface object
    # with white colour
    display_surface.fill((255, 250, 254))
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    for fires in firelist:
        if boom:
            fires.explosion()
        else:
            fires.update()
    newfire = fire(copy.copy(pos))
    
    if not boom:
        display_surface.blit(rot_center(image, angle), (pos[0]-100, pos[1]-100))
  
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.MOUSEBUTTONDOWN:
            explode()
            
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            quit()
  
        # Draws the surface object to the screen.  
    pygame.display.update()