from math import sqrt


def area(a, b, c):
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))
            and isinstance(c, (int, float))):
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        print("Wrong input")


def perimeter(a, b, c):
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))
            and isinstance(c, (int, float))):
        return a + b + c
    else:
        print("Wrong input")
