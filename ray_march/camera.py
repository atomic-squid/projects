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
    # generalized camera is still not implemented so projection is simple

    def __init__(self,
                 viewport: Viewport = Viewport(),
                 position: vec4 = vec4(),
                 rot: vec4 = vec4(),
                 fov: float = 70):
        self.__viewport = viewport
        self.__position = position
        self.__rot = rot
        self.__fov = fov

    @property
    def viewport(self):
        return self.__viewport
    
    @property
    def position(self):
        return self.__position
    
    @property
    def rot(self):
        return self.__rot
    
    @property
    def fov(self):
        return self.__fov
    
    def viewport_to_screenspace(self, viewport_x, viewport_y):
        """Transform a given coordiante to screen volume space"""
        scale = 2 / self.viewport.yres
        screen_x = viewport_x * scale - 1 * self.viewport.aspect
        screen_y = viewport_y * scale - 1
        screen_pos = vec4(screen_x, screen_y, 1)
        direction = (screen_pos - self.position).norm()
        return screen_pos, direction
    
if __name__ == "__main__":
    cam = Camera(Viewport())
    print(cam.viewport_to_screenspace(1,1))
    print(cam.viewport_to_screenspace(400,300))
    print(cam.viewport_to_screenspace(800,600))