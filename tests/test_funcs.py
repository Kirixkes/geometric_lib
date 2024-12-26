import unittest
from Funcs.calculate import calc
import circle
import square
import triangle

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
