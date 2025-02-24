import unittest
from Funcs import triangle


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(triangle.area(3, 4, 5), 6.0, places=4)
        self.assertAlmostEqual(triangle.area(5, 5, 5), 10.8253, places=4)
        self.assertAlmostEqual(triangle.area(10, 10, 10), 43.3013, places=4)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)
        self.assertEqual(triangle.perimeter(10, 10, 10), 30)


if __name__ == '__main__':
    unittest.main()
