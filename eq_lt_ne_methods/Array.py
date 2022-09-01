class Integer:
    def __init__(self, start_value:int=0):
        self.value = start_value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        if type(value) is int:
            self.__value = value
        else:
            raise ValueError('должно быть целое число')

class Array:
    def __init__(self, max_length:int=1, cell=Integer):
        self.max_length, self.cell, self.array = max_length, cell, {__: cell() for __ in range(max_length)}

    def __getitem__(self, key):
        self.check_value(key)
        return self.array[key].value

    def __setitem__(self, key, value):
        self.check_value(key)
        self.array[key].value = value

    def check_value(self, key):
        if type(key) is int and 0 <= key < self.max_length:
            return True
        raise IndexError('неверный индекс для доступа к элементам массива')

    def __str__(self) -> str:
        return " ".join([str(self.array[el].value) for el in self.array.keys()])


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)

try:
    ar_int[1] = 10.5 # должно генерироваться исключение ValueError
except ValueError:
    assert True
else:
    assert False, "must be int"

try:
    ar_int[10] = 1 # должно генерироваться исключение IndexError
except IndexError:
    assert True
else:
    assert False, "inex must be int"