import unittest
from math import floor

from Funcs.circle import area, perimeter

class TestCircleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(round(area(1), 5), 3.14159)
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(round(area(2), 5), 12.56637)
        self.assertAlmostEqual(round(area(5), 5), 78.53982)

    def test_perimeter(self):
        self.assertAlmostEqual(round(perimeter(1), 5), 6.28319)
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(round(perimeter(2), 5), 12.56637)
        self.assertAlmostEqual(round(perimeter(5), 5), 31.41593)

if __name__ == "__main__":
    unittest.main()
