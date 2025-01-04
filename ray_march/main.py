import pygame
from shapes import *
from camera import *
from datetime import datetime

# init game engine
pygame.init()

#screen parameters
viewport = Viewport(800, 600)
camera = Camera(viewport)

screen = pygame.display.set_mode((viewport.xres, viewport.yres))

# surface object to hold rendering data
surface = pygame.surface.Surface((viewport.xres, viewport.yres))

# raymarch
def raymarch(pos: vec4, dir: vec4, shapes):
    point = pos
    dist_traveled = 0.0
    for i in range(256):
        dist = min(shape.sdf(point) for shape in shapes)
        if dist < 0.001:
            break
        if dist_traveled > 1000:
            return (None, i)
        dist_traveled += dist
        point = pos + dir * dist_traveled
    return (dist_traveled, i)

# color based on distance
def shade(distance, iter):
    if distance is None:
        return (iter, iter, iter)
    else:
        # intensity = 255 - int(min(distance / vp.yres, 1) * 255)
        return (max(iter, 0), max(iter, 0), max(iter, 0))

# shape in world space
shapes = [Torus(vec4(0, x, 0), 0.5, 0.1) for x in (-0.3, 0.0, 0.3, 0.6)]


# update surface
# generalized camera is still not implemented so projections are orthographic
start = datetime.now()
dir = vec4(0, 1, 10).norm()
for x, y in ((x + 1, y + 1) for x in range(viewport.xres) for y in range(viewport.yres)):
    color = shade(*raymarch(vec4(*camera.get_screen_coord(x, y), -1), dir, shapes))
    surface.set_at((x, y), color)
end = datetime.now()
print(f"Render time: {end - start}")

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