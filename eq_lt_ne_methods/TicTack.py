class Cell:
    def __init__(self, value=0):
        self.value = value
 
    @property
    def is_free(self): 
        return self.value == 0

    @is_free.setter
    def is_free(self, value=False):
        pass

    def __bool__(self):
        return self.value == 0  

    def __str__(self):
         return str(self.value)  
    
class TicTacToe:
    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for __ in range(3)]

    def clear(self):
        self.__init__()

    def __getitem__(self, key):
        self.check_key(key)
        if type(key[0]) is int:
            # кей может быть инт и слайс
            return self.pole[key[0]][key[1]].value if type(key[1]) is int else tuple([el.value for el in self.pole[key[0]][key[1]]])
        elif type(key[0]) is slice:
            return tuple([self.pole[el][key[1]].value for el in range(0,3)][key[0]])
        else:
            return self.pole[key[0]][key[1]].value if type(key[1]) is int else tuple(self.pole[key[0]][key[1]].value)

    def __setitem__(self, key, value):
        # пока оставил кей толька инт
        if all(map(lambda x: type(x) is int and 0 <= x <3, key)):
            self.pole[key[0]][key[1]].value = value
        else:
            raise IndexError("Index must be 2 integers")

    def check_key(self, key):
        if len(key) < 2 or not all(map(lambda x: type(x) in {int, slice}, key)):
            raise ImportError("Index must be 2 integers or int and slice")

    def __str__(self):
        return '\n'.join([' '.join([str(i.value) for i in el]) for el in self.pole])

#tests

g = TicTacToe()
g.clear()
print(g)
print(g[0,0])
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
print(g[1,1])
print(g[2,1])

print(g)
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3
print(g)
assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"