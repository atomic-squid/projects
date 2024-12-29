# 3d graphics requires a lot of vector math so we'll
# define a vector class and bake in some math operators and methods

"""4-dimensional vector implementation"""

# 4d vector class
class Vec4:
    """A point in 4-dimensional space"""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    # string representation
    def __repr__(self): return f"Vec4({self.x}, {self.y}, {self.z}, {self.w})"

    # equality "self == other"
    def __eq__(self, other: "Vec4"):
        return (self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w)

    # negative "- self"
    def __neg__(self): return Vec4(- self.x, - self.y, - self.z, - self.w)
    
    # positive "+ self"
    def __pos__(self): return Vec4(+ self.x, + self.y, + self.z, + self.w)

    # addition "self + other"
    def __add__(self, other: "Vec4"):
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __iadd__(self, other: "Vec4"):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.w += other.w
        return self

    # subtraction "self - other"
    def __sub__(self, other: "Vec4"):
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    
    def __isub__(self, other: "Vec4"):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        self.w -= other.w
        return self

    # multiplication by a scalar "self * other"
    def __mul__(self, other: "float"):
        return Vec4(self.x * other,self.y * other,self.z * other,self.w * other)
    
    def __imul__(self, other: "float"):
        self.x *= other
        self.y *= other
        self.z *= other
        self.w *= other
        return self

    # divison by a scalar "self / other"
    def __truediv__(self, other: "float"):
        return Vec4(self.x / other,self.y / other,self.z / other,self.w / other)

    def __itruediv__(self, other: "float"):
        self.x /= other
        self.y /= other
        self.z /= other
        self.w /= other
        return self

    # dot product "self @ other"
    def dot(self, other: "Vec4"):
        """
        Computes the dot product of this vector with another Vec4 vector.

        Parameters:
            other (Vec4): The other vector to compute the dot product with.

        Returns:
            float: The dot product of this vector and the other vector.
        """
        return (self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w)
    
    # cross product "self ^ other"
    def cross(self, other: "Vec4"):
        """
        Computes the cross product of this vector with another Vec4 vector.

        Parameters:
            other (Vec4): The other vector to compute the cross product with.

        Returns:
            Vec4: A new vector that is the cross product of this vector and the other vector.
        """
        return Vec4(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
            0.0)
    
    # magnitude
    def mag(self):
        """
        Calculate the magnitude of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return (self.x**2 + self.y**2 + self.z**2 + self.w**2) ** 0.5
    
    # normal
    def norm(self):
        """
        Calculate the normalized version of this vector

        Returns:
            Vec4: The normal of the vector
        """
        return self / self.mag()