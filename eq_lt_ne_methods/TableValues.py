class Cell:
    def __init__(self, data=0):
        self.data = data
    
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value
    
class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows, self.cols, self.type_data = rows, cols, type_data
        self.table = tuple([tuple([Cell() for c in range(self.cols)]) for r in range(self.rows)])

    @staticmethod
    def TE():
        raise TypeError('неверный тип присваиваемых данных')

    @staticmethod
    def IE():
        raise IndexError('неверный индекс')

    def check_value(self, value):
        return value if type(value) == self.type_data else self.TE()

    def check_key(self, key):
        return key if 0 <= key[0] < self.rows and 0 <= key[1] < self.cols else self.IE()

    def __getitem__(self, key):
        r, c = self.check_key(key)
        return self.table[r][c].data

    def __setitem__(self, key, value):
        r, c = self.check_key(key)
        value = self.check_value(value)
        self.table[r][c].data = value

    def __iter__(self):
        for row in self.table:
            yield (el.data for el in row)


# tests
tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"
        
assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"


tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

