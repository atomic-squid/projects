from vector import *

class Viewport:
    def __init__(self, xres: int = 800, yres: int = 600):
        self.__xres = xres
        self.__yres = yres

    @property
    def xy(self):
        return (self.__xres, self.__yres)
    
    @property
    def xres(self):
        return self.__xres

    @property
    def yres(self):
        return self.__yres

    @property
    def aspect(self):
        return self.__xres / self.__yres
    
    def in_viewport(self, x, y):
        return 0 < x <= self.xres and 0 < y <= self.yres

class Camera:
    def __init__(self,
                 viewport: Viewport = Viewport(),
                 pos: vec4 = vec4(),
                 rot: vec4 = vec4(),
                 fov: float = 70):
        self.__viewport = viewport
        self.__pos = pos
        self.__rot = rot
        self.__fov = fov

    @property
    def viewport(self):
        return self.__viewport
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def rot(self):
        return self.__rot
    
    @property
    def fov(self):
        return self.__fov
    
    def get_screen_coord(self, viewport_x, viewport_y):
        """Transform a given coordiante to screen volume space"""
        scale = 2 / self.viewport.yres
        screen_x = viewport_x * scale - 1 * self.viewport.aspect
        screen_y = viewport_y * scale - 1
        return (screen_x, screen_y)
    
if __name__ == "__main__":
    cam = Camera(Viewport())
    print(cam.get_screen_coord(1,1))
    print(cam.get_screen_coord(400,300))
    print(cam.get_screen_coord(800,600))