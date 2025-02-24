
def area(a):
    if isinstance(a, (int, float)):
        return a * a
    else:
        print("Wrong input")


def perimeter(a):
    if isinstance(a, (int, float)):
        return 4 * a
    else:
        print("Wrong input")
