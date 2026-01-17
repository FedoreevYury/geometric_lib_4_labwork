import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        res = area(-5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_perimeter_positive(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative(self):
        res = perimeter(-5)
        self.assertAlmostEqual(res, -31.41592653589793)

if __name__ == '__main__':
    unittest.main()


