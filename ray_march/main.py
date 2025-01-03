import pygame

# init game engine
pygame.init()

#screen parameters
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# surface object to hold rendering data
surface = pygame.surface.Surface((screen_width, screen_height))

# signed distance function
def sdf(x, y, z):
    # circle is hardcoded
    center_x = screen_width // 2
    center_y = screen_height // 2
    center_z = screen_height
    radius = 200
    # calculate xy deltas
    delta_x = x - center_x
    delta_y = y - center_y
    delta_z = z - center_z
    return (delta_x ** 2 + delta_y ** 2 + delta_z ** 2) ** 0.5 - radius

# raymarch
def raymarch(x, y):
    # this version assumes we march straight down the z axis in a simple ortographic projection
    point = (x, y, 0) # start at 0 on the z axis
    dist_traveled = 0.0
    for i in range(256):
        dist = sdf(*point)
        if dist < 0.01:
            break
        if dist_traveled > 10000:
            return (None, i)
        dist_traveled += dist
        point = (*point[:2], dist_traveled)
    return (dist_traveled, i)

# color based on distance
def shade(distance, iter):
    if distance is None:
        intensity = 0
    else:
        intensity = 255 - int(min(distance / 1000, 1) * 255)
    return (max(iter, intensity), max(iter, 0), max(iter, intensity))

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
    screen.fill("black")

    # update surface
    for x, y in ((x + 1, y + 1) for x in range(screen_width) for y in range(screen_height)):
        surface.set_at((x, y), shade(*raymarch(x, y)))

    screen.blit(surface, (0, 0))

    # update display
    pygame.display.flip()

    clock.tick(60) # limit to 60fps

pygame.quit()