from time import time
NUM = {int, float}

class Vector:
    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        if all(map(lambda x: type(x) in NUM, value)) or value == tuple():
            self.__coords = value
        else:
            raise ValueError('координаты должны быть числами')

    def __init__(self, *args) -> None:
        self.coords = args if args else tuple()

    def get_coords(self):
        return self.coords
            
    def __len__(self):
        return len(self.coords) 

    def __add__(self, other):
        self.check_o(other)
          
        if type(other) in NUM:
            return __class__(*[el + other for el in self.coords])
        else:
            return __class__(*[el + other.coords[i] for i, el in enumerate(self.coords)])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self.check_o(other)
        if type(other) in NUM:
            return __class__(*[el - other for el in self.coords])
        else:
            return __class__(*[el - other.coords[i] for i, el in enumerate(self.coords)])

    def __rsub__(self, other):
        return self.__sub__(other)

    def __eq__(self, __o: object) -> bool:
        return True if self.coords == __o.coords else False

    def __mul__(self, other):
        self.check_o(other)
        if type(other) in NUM:
            return __class__(*[el * other for el in self.coord])
        else:
            return __class__(*[el * other.coords[i] for i, el in enumerate(self.coords)])

    def __rmul__(self, other):
        return self.__mul__(other)

    def check_o(self, other):
        if isinstance(other, Vector) and len(other) != len(self):
            raise ArithmeticError('размерности векторов не совпадают')
        else:
            if not isinstance(other, (int, float, Vector)):
                raise ValueError("Other argument must be a number or Vector")

class VectorInt(Vector):
    def check_int(self, value):
        return all(map(lambda x: type(x) is int, value)) or value == tuple()

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        if self.check_int(value):
            self.__coords = value
        else:
            raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        res = super().__add__(other)
        return self.__class__(*res.coords) if self.check_int(res.get_coords()) else res
    
    def __sub__(self, other):
        res = super().__sub__(other)
        return self.__class__(*res.coords) if self.check_int(res.get_coords()) else res

    def __mul__(self, other):
        res = super().__mul__(other)
        return self.__class__(*res.coords) if self.check_int(res.get_coords()) else res


t1 = time()
v0 = Vector(0)
print(v0.coords)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
V3 = VectorInt(0, 1, 2, 3)
v4 = V3 + 4.5
print(v4.coords, type(v4))
v5 = V3 + 6
print(v5.coords, type(v5))
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True

# тесті
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

    
v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1+v2
assert type(v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1+v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
t2 = time()
print(t2-t1)