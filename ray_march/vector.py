class vec4:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0, w = 0.0):
        if not all(isinstance(val, (float, int)) for val in (x, y, z, w)):
            raise ValueError("x, y, z, w values must all be of value float or integer")
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__w = float(w)

    def __repr__(self):
        return f"vec4({self.__x}, {self.__y}, {self.__z}, {self.w})"
    
    def __add__(self, other: "vec4"):
        return vec4(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w)

    def __sub__(self, other: "vec4"):
        return vec4(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w)
    
    def __mul__(self, other: float):
        return vec4(
            self.x * other,
            self.y * other,
            self.z * other,
            self.w * other)
    
    def __truediv__(self, other: float):
        return vec4(
            self.x / other,
            self.y / other,
            self.z / other,
            self.w / other)

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
    def w(self):
        return self.__w

    @property
    def xyzw(self):
        return (self.__x, self.__y, self.__z, self.__w)
    
    def mag(self, other = None):
        if other is None:
            other = vec4()
        vector = self - other
        return (vector.x ** 2 + vector.y ** 2 + vector.z ** 2 + vector.w ** 2) ** 0.5
    
    def norm(self, other = None):
        if other is None:
            other = vec4()
        vector = self - other
        magnitude = self.mag(other)
        return vector / magnitude