import unittest

from Funcs.square import area, perimeter

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)

    def test_perimeter(self):
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)

if __name__ == "__main__":
    unittest.main()
