from vector import *

class Shape:
    def __init__(self, center: vec4 = None):
        if center is None:
            self.__center = vec4(0.0, 0.0, 0.0)
            return self
        self.__center = center
        return self

    @property
    def center(self):
        return self.__center

class Sphere(Shape):
    def __init__(self, center: vec4, radius = 1.0):
        if not isinstance(radius, (float, int)):
            raise ValueError("radius must be a float or integer value")
        if radius < 0:
            raise ValueError("radius cannot be negative")
        super().__init__(center)
        self.__radius = radius
    
    def __repr__(self):
        return f"Sphere({self.center}, {self.radius})"
    
    @property
    def radius(self):
        return self.__radius
    
    # signed distance function
    def sdf(self, pos: vec4):
        return self.center.mag(pos) - self.radius

class Torus(Shape):
    def __init__(self, center: vec4, major_r: int = 0.0, minor_r: int = 0.0):
        for val in (major_r, minor_r):
            assert isinstance(val, (float, int)), "value must be a float or integer value"
            assert val >= 0, "value cannot be negative"               
        super().__init__(center)
        self.__major_r = major_r
        self.__minor_r = minor_r

    def __repr__(self):
        return f"Torus({self.center}, {self.major_r}, {self.minor_r})"
    
    @property
    def major_r(self):
        return self.__major_r

    @property
    def minor_r(self):
        return self.__minor_r

    # signed distance function
    def sdf(self, pos: vec4):
        vector = self.center - pos
        major = (vector.x ** 2 + vector.z ** 2) ** 0.5 - self.major_r
        return (major ** 2 + vector.y ** 2) ** 0.5 - self.minor_r