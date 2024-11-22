import math

def area(r):
    if isinstance(r, (int, float)):
        return math.pi * r * r
    else:
        print("Wrong input")


def perimeter(r):
    if isinstance(r, (int, float)):
        return 2 * math.pi * r
    else:
        print("Wrong input")

