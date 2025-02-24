import unittest
from Funcs import circle


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(round(circle.area(1), 5), 3.14159)
        self.assertEqual(circle.area(0), 0)
        self.assertAlmostEqual(round(circle.area(2), 5), 12.56637)
        self.assertAlmostEqual(round(circle.area(5), 5), 78.53982)

    def test_perimeter(self):
        self.assertAlmostEqual(round(circle.perimeter(1), 5), 6.28319)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertAlmostEqual(round(circle.perimeter(2), 5), 12.56637)
        self.assertAlmostEqual(round(circle.perimeter(5), 5), 31.41593)


if __name__ == '__main__':
    unittest.main()
