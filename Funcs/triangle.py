from math import sqrt

def area(a, b, c):
    if isinstance(a,b,c, (int, float)):
        return sqrt(((a + b + c) / 2) * (((a + b + c) / 2) - a)
                * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c))
    else:
        print("Wrong input")

def perimeter(a, b, c):
    if isinstance(a, b, c, (int, float)):
        return a + b + c
    else:
        print("Wrong input")
