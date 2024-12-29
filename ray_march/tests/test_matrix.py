import unittest
from matrix import Mat4, identity

class TestMat4(unittest.TestCase):
    def test_init_empty(self):
        m = Mat4()
        self.assertEqual(m.data, [[0.0]*4 for _ in range(4)])

    def test_init_with_data(self):
        data = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
        m = Mat4(data)
        self.assertEqual(m.data, data)

    def test_init_invalid_rows(self):
        data = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
        with self.assertRaises(AssertionError):
            Mat4(data)

    def test_init_invalid_cols(self):
        data = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        with self.assertRaises(AssertionError):
            Mat4(data)

    def test_equality(self):
        m1 = Mat4([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
        m2 = Mat4([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
        m3 = Mat4([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
        self.assertEqual(m1, m2)
        self.assertNotEqual(m1, m3)

    def test_negation(self):
        m = Mat4([[1,2,3,4], [-5,6,-7,8], [9,-10,11,-12], [-13,14,-15,16]])
        expected = Mat4([[-1,-2,-3,-4], [5,-6,7,-8], [-9,10,-11,12], [13,-14,15,-16]])
        self.assertEqual(-m, expected)

    def test_addition(self):
        m1 = Mat4([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
        m2 = Mat4([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]])
        expected = Mat4([[2,3,4,5], [7,8,9,10], [12,13,14,15], [17,18,19,20]])
        self.assertEqual(m1 + m2, expected)

    def test_subtraction(self):
        m1 = Mat4([[2,3,4,5], [7,8,9,10], [12,13,14,15], [17,18,19,20]])
        m2 = Mat4([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]])
        expected = Mat4([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
        self.assertEqual(m1 - m2, expected)

    def test_matrix_multiplication(self):
        m1 = Mat4([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
        m2 = Mat4([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
        self.assertEqual(m1 @ m2, m2)
        self.assertEqual(m2 @ m1, m2)

    def test_identity(self):
        m = Mat4([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
        self.assertEqual(m @ identity, m)
        self.assertEqual(identity @ m, m)

if __name__ == '__main__':
    unittest.main()