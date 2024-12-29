# 3d graphics requires a lot of vector math so we'll
# define a vector class and bake in some math operators and methods

from typing import List
import math

"""4-dimensional vector implementation"""

def dot(a: List[float], b: List[float]) -> float:
    assert len(a) == 4, "a must be a 4 element list"
    assert len(b) == 4, "b must be a 4 element list"
    return sum(x * y for x, y in zip(a, b))


def cross(a: List[float], b: List[float]) -> List[float]:
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
        0.0]

# 4d vector class
class Vec4:
    """A point in 4-dimensional space"""

    def __init__(self, x: float, y: float, z: float, w: float):
        self.data = [float(x), float(y), float(z), float(w)]
    
    @property
    def x(self) -> float:
        return self.data[0]
    
    @property
    def y(self) -> float:
        return self.data[1]
    
    @property
    def z(self) -> float:
        return self.data[2]
    
    @property
    def w(self) -> float:
        return self.data[3]
    
    def __eq__(self, other: "Vec4") -> bool:
        return self.data == other.data
    
    def __neg__(self) -> "Vec4":
        return Vec4(-self.data[0], -self.data[1], -self.data[2], -self.data[3])
    
    def __add__(self, other: "Vec4") -> "Vec4":
        return Vec4(*(a + b for a, b in zip(self.data, other.data)))
    
    def __iadd__(self, other: "Vec4") -> "Vec4":
        self.data = [a + b for a, b in zip(self.data, other.data)]
        return self
    
    def __sub__(self, other: "Vec4") -> "Vec4":
        return Vec4(*(a - b for a, b in zip(self.data, other.data)))
    
    def __isub__(self, other: "Vec4") -> "Vec4":
        self.data = [a - b for a, b in zip(self.data, other.data)]
        return self
    
    def __mul__(self, scalar: float) -> "Vec4":
        return Vec4(*(x * scalar for x in self.data))
    
    def __rmul__(self, scalar: float) -> "Vec4":
        return self * scalar
    
    def __truediv__(self, scalar: float) -> "Vec4":
        return Vec4(*(x / scalar for x in self.data))
    
    def __rtruediv__(self, scalar: float) -> "Vec4":
        return self / scalar

    def __str__(self) -> str:
        return f"Vec4({self.x}, {self.y}, {self.z}, {self.w})"
    
    def dot(self, other: "Vec4") -> float:
        return dot(self.data, other.data)
    
    def cross(self, other: "Vec4") -> "Vec4":
        result = cross(self.data, other.data)
        return Vec4(*result)
    
    def length(self) -> float:
        return math.sqrt(self.dot(self))
    
    def normalize(self) -> "Vec4":
        length = self.length()
        if length > 0:
            return Vec4(*(x/length for x in self.data))
        return Vec4(0, 0, 0, 0)