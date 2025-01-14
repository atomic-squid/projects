import pygame
from shapes import *
from camera import *
from vector import *
from datetime import datetime

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
def raymarch_shade(distance, iter):
    if distance is None:
        return pygame.Color(iter, iter, iter)
    else:
        intensity = 255 - int(min(distance / 2, 1) * 255)
        return pygame.Color(max(iter, 0), max(iter, intensity), max(iter, 0))

# render point
def render_point(camera: Camera, point, shapes):
    pos, dir = camera.viewport_to_screenspace(*point)
    result = raymarch(pos, dir, shapes)
    color = raymarch_shade(*result)
    return point, color


if __name__ == "__main__":
    # init game engine
    pygame.init()

    #screen parameters
    viewport = Viewport(1280, 720)
    camera = Camera(viewport, vec4(0, 0, 4))

    screen = pygame.display.set_mode(viewport.xy)

    # surface object to hold rendering data
    surface = pygame.surface.Surface(viewport.xy)

    # shape in world space
    shapes = [Torus(vec4(0, x, 0), 0.75, 0.1) for x in (-0.3, 0.0, 0.3)]
    for shape in shapes:
        print(shape)

    # update surface
    start = datetime.now()
    points = [[(x + 1, y + 1) for x in range(viewport.xres)] for y in range(viewport.yres)]
    for row in points:
        for point in row:
            result = render_point(camera, point, shapes)
            surface.set_at(*result)
        screen.blit(surface, (0, 0))
        pygame.display.flip()

    end = datetime.now()
    print(f"Render time: {end - start}")

    # output surface to image
    pygame.image.save(surface, "render.png")

    # title
    pygame.display.set_caption("Ray March Rendering")

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()