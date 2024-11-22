import unittest
from Funcs.calculate import calc, figs, funcs
import circle
import square

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        result = calc('circle', 'area', [5])
        expected = circle.area(5)
        self.assertEqual(result, f'area of circle is {expected}')

    def test_square_area(self):
        result = calc('square', 'area', [4])
        expected = square.area(4)
        self.assertEqual(result, f'area of square is {expected}')

    def test_circle_perimeter(self):
        result = calc('circle', 'perimeter', [5])
        expected = circle.perimeter(5)
        self.assertEqual(result, f'perimeter of circle is {expected}')

    def test_square_perimeter(self):
        result = calc('square', 'perimeter', [4])
        expected = square.perimeter(4)
        self.assertEqual(result, f'perimeter of square is {expected}')

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'area', [3])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])

if __name__ == '__main__':
    unittest.main()