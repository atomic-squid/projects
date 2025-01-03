class Triplet:
    def __init__(self, x, y, z):
        if not all(isinstance(val, (float, int)) for val in (x, y, z)):
            raise ValueError("x, y, z values must all be of value float or integer")
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    def __repr__(self):
        return f"Triplet({self.__x}, {self.__y}, {self.__z})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @property
    def xyz(self):
        return (self.__x, self.__y, self.__z)

class Shape:
    def __init__(self, center: Triplet = None):
        if center is None:
            self.__center = Triplet(0.0, 0.0, 0.0)
            return self
        self.__center = center
        return self

    @property
    def center(self):
        return self.__center


class Sphere(Shape):
    def __init__(self, center: Triplet, radius = 1.0):
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
    def sdf(self, pos: Triplet):
        return ((self.center.x - pos.x) ** 2 + (self.center.y - pos.y) ** 2 + (self.center.z - pos.z) ** 2) ** 0.5 - self.radius