import unittest
from Funcs.triangle import area, perimeter

class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=5)
        self.assertAlmostEqual(area(5, 5, 5), 10.8253, places=5)
        self.assertAlmostEqual(area(10, 10, 10), 43.3013, places=5)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)
        self.assertEqual(perimeter(10, 10, 10), 30)

if __name__ == "__main__":
    unittest.main()
