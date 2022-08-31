from time import time
NUM = {int, float}

class Vector:
    def __init__(self, *args) -> None:
        self.coords = args if args else tuple()
            
    def __len__(self):
        return len(self.coords) 

    def __add__(self, other):
        self.check_o(other)
          
        if type(other) in NUM:
            return Vector(*[el + other for el in self.coords])
        else:
            return Vector(*[el + other.coords[i] for i, el in enumerate(self.coords)])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self.check_o(other)

        if type(other) in NUM:
            return Vector(*[el - other for el in self.coords])
        else:
            return Vector(*[el - other.coords[i] for i, el in enumerate(self.coords)])

    def __rsub__(self, other):
        return self.__sub__(other)

    def __eq__(self, __o: object) -> bool:
        return True if self.coords == __o.coords else False

    def __mul__(self, other):
        self.check_o(other)
        if type(other) in NUM:
            return Vector(*[el * other for el in self.coord])
        else:
            return Vector(*[el * other.coords[i] for i, el in enumerate(self.coords)])

    def __rmul__(self, other):
        return self.__mul__(other)

    def check_o(self, other):
        if type(other) == type(self) and len(other) != len(self):
            raise ArithmeticError('размерности векторов не совпадают')
        else:
            if type(other) not in {int, float, Vector}:
                raise ValueError("Other argument must be a number or Vector")
t1 = time()
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
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
t2 = time()
print(t2-t1)