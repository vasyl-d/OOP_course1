NUM = {int, float}

def VE(msg="некорректные координаты и параметры прямоугольника"):
    raise ValueError(msg)

def TE():
    raise TypeError('прямоугольники пересекаются')

class Number:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 

    def __set__(self, instance, value):
        if type(value) not in {int, float}:
            VE()
        setattr(instance, self.name, value)            

class PositiveNumber(Number):
    def __set__(self, instance, value):
        if type(value) not in {int, float} or value <=0:
            VE()
        setattr(instance, self.name, value)

class Rect:
    _x = Number()
    _y = Number()
    _width = PositiveNumber()
    _height = PositiveNumber()
    def __init__(self, x, y, width, height):
        self._x, self._y, self._width, self._height = x, y, width, height

    def is_collision(self, other):
        # //two rectangles intersection
        # A.X1 < B.X2:	true
        # A.X2 > B.X1:	true
        # A.Y1 < B.Y2:	true
        # A.Y2 > B.Y1:	true
        # Intersect:	true
        if (self._x < other._x + other._width and self._x + self._width > other._x and self._y < other._y + other._height and self._y + self._height > other._y):
            TE()
        else:
            return False

    def __str__(self):
        return f"x: {self._x} y: {self._y} width: {self._width} height: {self._height}"


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True


lst_not_collision = list(filter(not_collision, lst_rect))

print(*lst_not_collision)

# tests

r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
