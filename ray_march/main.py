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
def raymarch(pos: vec4, dir: vec4, shape):
    point = pos
    dist_traveled = 0.0
    for i in range(256):
        dist = shape.sdf(point)
        if dist < 0.01:
            break
        if dist_traveled > 10000:
            return (None, i)
        dist_traveled += dist
        point = pos + dir * dist_traveled
    return (dist_traveled, i)

# color based on distance
def shade(distance, iter):
    if distance is None:
        return (iter, iter, iter)
    else:
        # intensity = 255 - int(min(distance / screen_height, 1) * 255)
        return (
            max(iter, 0),
            max(iter, 0),
            max(iter, 0))

# shape
pos = vec4(screen_width // 2, screen_height // 2, screen_height // 2)
# shape = Sphere(pos, 200)
shape = Torus(pos, 200, 25)

# update surface
# generalized camera is still not implemented so projections are orthographic
dir = vec4(0, 1, 10).norm()
for x, y in ((x + 1, y + 1) for x in range(screen_width) for y in range(screen_height)):
    color = shade(*raymarch(vec4(x, y), dir, shape))
    surface.set_at((x, y), color)

# output surface to image
pygame.image.save(surface, "render.png")

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