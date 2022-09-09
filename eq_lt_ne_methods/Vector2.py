from time import time
NUM = {int, float}

class RadiusVector:
    def __init__(self, *args) -> None:
        self.coords = list(args) if args else []
            
    def __len__(self):
        return len(self.coords) 

    def __add__(self, other):
        self.check_o(other)
          
        if type(other) in NUM:
            return RadiusVector(*[el + other for el in self.coords])
        else:
            return RadiusVector(*[el + other.coords[i] for i, el in enumerate(self.coords)])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self.check_o(other)

        if type(other) in NUM:
            return RadiusVector(*[el - other for el in self.coords])
        else:
            return RadiusVector(*[el - other.coords[i] for i, el in enumerate(self.coords)])

    def __rsub__(self, other):
        return self.__sub__(other)

    def __eq__(self, __o: object) -> bool:
        return True if self.coords == __o.coords else False

    def __mul__(self, other):
        self.check_o(other)
        if type(other) in NUM:
            return RadiusVector(*[el * other for el in self.coord])
        else:
            return RadiusVector(*[el * other.coords[i] for i, el in enumerate(self.coords)])

    def __rmul__(self, other):
        return self.__mul__(other)

    def check_o(self, other):
        if type(other) == type(self) and len(other) != len(self):
            raise ArithmeticError('размерности векторов не совпадают')
        else:
            if type(other) not in {int, float, RadiusVector}:
                raise ValueError("Other argument must be a number or Vector")

    def __getitem__(self, key):
        self.ch_key(key)
        return self.coords[key] if type(key) is int else tuple(self.coords[key])

    def __setitem__(self, key, value):
        self.ch_key(key)
        if type(key) is slice and len(value) > len(self):
            raise IndexError("Index out of range")
        self.coords[key] = value


    def ch_key(self, key):
        if type(key) is int and 0 <= key <= len(self): 
            return True
        elif type(key) is slice:
            return True
        raise IndexError("index out of range")

    def __str__(self):
        return ' '.join([str(el) for el in self.coords])

#tests

t1 = time()
v1 = RadiusVector(1, 2, 3)
v2 = RadiusVector(4, 5, 6)
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


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5


try:
    print(v[6])
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось ошибка IndexError при получении значенияза пределами"

print(v[:])
try:
    v[0:6] = 1,2,3,4,5,6
except Exception as Ex:
    assert True
else:
    assert False, "не сгенерировалось ошибка IndexError при обновлении значений"
print(v)
t2 = time()
print(t2-t1)