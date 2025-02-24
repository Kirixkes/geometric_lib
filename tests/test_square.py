import unittest
from Funcs import square


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(1), 4)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(5), 20)


if __name__ == '__main__':
    unittest.main()
