import unittest
from vector import Vec4

class TestVec4(unittest.TestCase):

    def test_initialization(self):
        v = Vec4(1, 2, 3, 4)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)
        self.assertEqual(v.w, 4)

    def test_equation(self):
        self.assertEqual(Vec4(1, 2, 3, 4), Vec4(1, 2, 3, 4))

    def test_addition(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(4, 3, 2, 1)
        v3 = v1 + v2
        self.assertEqual(v3, Vec4(5, 5, 5, 5))

    def test_subtraction(self):
        v1 = Vec4(5, 6, 7, 8)
        v2 = Vec4(1, 2, 3, 4)
        v3 = v1 - v2
        self.assertEqual(v3, Vec4(4, 4, 4, 4))

    def test_negation(self):
        v = Vec4(1, -2, 3, -4)
        self.assertEqual(-v, Vec4(-1, 2, -3, 4))

    def test_multiplication(self):
        v = Vec4(1, 2, 3, 4)
        self.assertEqual(v * 2, Vec4(2, 4, 6, 8))

    def test_division(self):
        v = Vec4(2, 4, 6, 8)
        self.assertEqual(v / 2, Vec4(1, 2, 3, 4))

    def test_dot_product(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(4, 3, 2, 1)
        self.assertEqual(v1.dot(v2), 20)

    def test_cross_product(self):
        v1 = Vec4(1, 2, 3, 0)
        v2 = Vec4(4, 5, 6, 0)
        self.assertEqual(v1.cross(v2), Vec4(-3, 6, -3, 0))

    def test_magnitude(self):
        v = Vec4(1, 2, 2, 1)
        self.assertAlmostEqual(v.mag(), 3.1622776601683795)

    def test_normalization(self):
        v = Vec4(1, 2, 2, 1)
        self.assertAlmostEqual(v.norm().mag(), 1.0)

if __name__ == '__main__':
    unittest.main()