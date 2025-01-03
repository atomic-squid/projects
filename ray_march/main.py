import pygame
from shapes import *

# init game engine
pygame.init()

#screen parameters
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# surface object to hold rendering data
surface = pygame.surface.Surface((screen_width, screen_height))

# raymarch
def raymarch(x, y, shape):
    # this version assumes we march straight down the z axis in a simple ortographic projection
    point = Triplet(x, y, 0) # start at 0 on the z axis
    dist_traveled = 0.0
    for i in range(256):
        dist = shape.sdf(point)
        if dist < 0.01:
            break
        if dist_traveled > 10000:
            return (None, i)
        dist_traveled += dist
        point = Triplet(point.x, point.y, dist_traveled)
    return (dist_traveled, i)

# color based on distance
def shade(distance, iter):
    if distance is None:
        intensity = 0
    else:
        intensity = 255 - int(min(distance / 1000, 1) * 255)
    return (max(iter, intensity), max(iter, 0), max(iter, intensity))

# sphere
sphere = Sphere(Triplet(screen_width // 2, screen_height // 2, screen_height // 2), 200)
print(sphere)

# update surface
for x, y in ((x + 1, y + 1) for x in range(screen_width) for y in range(screen_height)):
    surface.set_at((x, y), shade(*raymarch(x, y, sphere)))

# clock
clock = pygame.time.Clock()

# title
pygame.display.set_caption("Ray March Rendering")

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear screen
    screen.blit(surface, (0, 0))

    # update display
    pygame.display.flip()

    clock.tick(60) # limit to 60fps

pygame.quit()