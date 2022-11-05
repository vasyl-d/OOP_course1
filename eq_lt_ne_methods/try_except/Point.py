class Point:
    __slots__ = '_x','_y'
    def __init__(self, x=0, y=0):
        self._x, self._y = x, y

a, b = input().split()

try:
    pt = Point(int(a), int(b))

except ValueError:
    try:
        pt = Point(float(a), float(b))
    except ValueError:
        pt = Point()
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")