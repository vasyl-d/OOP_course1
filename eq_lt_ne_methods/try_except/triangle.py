NUM = {int, float}

def isItTriangle(a, b, c):
    s = (a, b, c)
    if all(map(lambda x: type(x) in NUM and x > 0, s)):
        if a + b > c and b + c > a and c + a > b:
            return True
        else:
            raise ValueError('из указанных длин сторон нельзя составить треугольник') 
    else:
        raise TypeError('стороны треугольника должны быть положительными числами')

class Triangle:
    __slots__ = '_a', '_b', '_c'

    def __init__(self, a, b, c) -> None:
        if isItTriangle(a, b, c):
            self._a, self._b, self._c = a, b, c
        
    def __str__(self):
        return f"Triangle: {self._a}*{self._b}*{self._c}"


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for x in input_data:
    try:
        isItTriangle(*x)
        lst_tr.append(Triangle(*x))
    except:
        pass

print(*lst_tr)

