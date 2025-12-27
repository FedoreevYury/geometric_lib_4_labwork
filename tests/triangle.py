import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(6, 4)
        self.assertEqual(res, 12)

    def test_area_zero(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        res = area(-6, 4)
        self.assertEqual(res, -12)

    def test_perimeter_positive(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_negative(self):
        res = perimeter(-1, 2, 3)
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()

