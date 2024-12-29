# Matrices!

from typing import List
from vector import dot

class Mat4:
    """
    A class to represent a 4x4 matrix and perform matrix operations.
    """

    # initalization
    def __init__(self, array: List[List[float]] = None):
        if array is None:
            self.data = [[0.0 for n in range(4)] for row in range(4)]
            return
        assert len(array) == 4, "Input array must have exactly 4 rows"
        assert all(len(row) == 4 for row in array), "Each row in the input array must have exactly 4 elements"
        self.data = array

    # string representation
    def __repr__(self):
        return repr(self.data)

    # equation "self == other"
    def __eq__(self, other: "Mat4"):
        for i in range(4):
            for j in range(4):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    # negative "- self"
    def __neg__(self):
        result = Mat4()
        for i in range(4):
            for j in range(4):
                result.data[i][j] = - self.data[i][j]
        return result

    # positive "+ self"
    def __pos__(self):
        result = Mat4()
        for i in range(4):
            for j in range(4):
                result.data[i][j] = + self.data[i][j]
        return result

    # addition "self + other"
    def __add__(self, other: "Mat4"):
        result = Mat4()
        for i in range(4):
            for j in range(4):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __iadd__(self, other: "Mat4"):
        for i in range(4):
            for j in range(4):
                self.data[i][j] += other.data[i][j]
        return self

    # subtraction "self - other"
    def __sub__(self, other: "Mat4"):
        result = Mat4()
        for i in range(4):
            for j in range(4):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __isub__(self, other: "Mat4"):
        for i in range(4):
            for j in range(4):
                self.data[i][j] -= other.data[i][j]
        return self

    # matrix multiplication "self @ other"
    def __matmul__(self, other: "Mat4"):
        result = Mat4()
        for i in range(4):
            for j in range(4):
                result.data[i][j] = dot(self.data[i], [row[j] for row in other.data])
        return result


# identity matrix
identity = Mat4([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])