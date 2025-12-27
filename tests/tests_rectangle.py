import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(5, 3)
        self.assertEqual(res, 15)

    def test_area_zero(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        res = area(-5, 3)
        self.assertEqual(res, -15)

    def test_perimeter_positive(self):
        res = perimeter(5, 3)
        self.assertEqual(res, 16)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()

