import unittest
from vector import Vec4, dot, cross

class TestVec4(unittest.TestCase):

    def test_initialization(self):
        v = Vec4(1, 2, 3, 4)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)
        self.assertEqual(v.w, 4)

    def test_equality(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(1, 2, 3, 4)
        v3 = Vec4(4, 3, 2, 1)
        self.assertTrue(v1 == v2)
        self.assertFalse(v1 == v3)

    def test_negation(self):
        v = Vec4(1, -2, 3, -4)
        self.assertEqual(-v, Vec4(-1, 2, -3, 4))

    def test_addition(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(4, 3, 2, 1)
        self.assertEqual(v1 + v2, Vec4(5, 5, 5, 5))

    def test_inplace_addition(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(4, 3, 2, 1)
        v1 += v2
        self.assertEqual(v1, Vec4(5, 5, 5, 5))

    def test_subtraction(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(4, 3, 2, 1)
        self.assertEqual(v1 - v2, Vec4(-3, -1, 1, 3))

    def test_inplace_subtraction(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(4, 3, 2, 1)
        v1 -= v2
        self.assertEqual(v1, Vec4(-3, -1, 1, 3))

    def test_multiplication(self):
        v = Vec4(1, 2, 3, 4)
        self.assertEqual(v * 2, Vec4(2, 4, 6, 8))

    def test_inplace_multiplication(self):
        v = Vec4(1, 2, 3, 4)
        v *= 2
        self.assertEqual(v, Vec4(2, 4, 6, 8))

    def test_division(self):
        v = Vec4(2, 4, 6, 8)
        self.assertEqual(v / 2, Vec4(1, 2, 3, 4))

    def test_inplace_division(self):
        v = Vec4(2, 4, 6, 8)
        v /= 2
        self.assertEqual(v, Vec4(1, 2, 3, 4))

    def test_dot_product(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)
        self.assertEqual(v1.dot(v2), 70)
    
    def test_standalone_dot_product(self):
        v1 = [1, 2, 3, 4]
        v2 = [5, 6, 7, 8]
        self.assertEqual(dot(v1, v2), 70)

    def test_cross_product(self):
        v1 = Vec4(1, 2, 3, 0)
        v2 = Vec4(4, 5, 6, 0)
        self.assertEqual(v1.cross(v2), Vec4(-3, 6, -3, 0))

    def test_standalone_cross_product(self):
        v1 = [1, 2, 3, 0]
        v2 = [4, 5, 6, 0]
        self.assertEqual(cross(v1, v2), [-3, 6, -3, 0])

    def test_magnitude(self):
        v = Vec4(1, 2, 2, 1)
        self.assertAlmostEqual(v.length(), 3.1622776601683795)

    def test_normalization(self):
        v = Vec4(1, 2, 2, 1)
        self.assertAlmostEqual(v.normalize(), Vec4(
            0.31622776601683794,
            0.6324555320336759,
            0.6324555320336759,
            0.31622776601683794))

if __name__ == '__main__':
    unittest.main()