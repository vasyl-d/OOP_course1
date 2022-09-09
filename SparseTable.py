class Cell:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
        
class SparseTable:
    def __init__(self):
        self.cells = {}

    @property
    def rows(self):
        return max([el[0] for el in self.cells.keys()])+1 if len(self.cells) > 0 else 0
    @rows.setter
    def rows(self, value):
        pass

    @property
    def cols(self):
        return max([el[1] for el in self.cells.keys()])+1 if len(self.cells) > 0 else 0
    @cols.setter
    def cols(self, value):
        pass

    @staticmethod
    def VE():
        raise ValueError('данные по указанным индексам отсутствуют')

    @staticmethod
    def IE():
        raise IndexError('ячейка с указанными индексами не существует')

    def checkindex(self, row, col):
        return True if type(row) is int and type(col) is int and 0 <= row and 0 <= col else self.IE()

    def add_data(self, row, col, data):
        #  - добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа);
        self.checkindex(row, col)
        if (row, col) not in self.cells:
            self.cells[(row, col)] = Cell(data)

    def remove_data(self, row, col):
        #  - удаление ячейки (объект класса Cell) с индексами (row, col).
        self.checkindex(row, col)
        return self.cells.pop((row, col)) if (row, col) in self.cells else self.IE()   

    def __getitem__(self, key):
        row, col = key
        self.checkindex(row, col)
        return self.cells[(row, col)].value if (row, col) in self.cells else self.VE()

    def __setitem__(self, key, value):
        row, col = key
        self.checkindex(row, col)
        self.cells[(row, col)] = Cell(value)

    def __delitem__(self, key):
        self.checkindex(key)
        return self.cells.pop(key) if key in self.cells else self.IE()        

    def __str__(self):
        return '\n'.join([f"cell{i}: {str(self.cells[i])}" for i in self.cells])

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице


# tests

st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
print(st[3,2])
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"
print(st)
st.remove_data(1, 1)
try:
    v = st[1, 1]
    print("st[1,1]", st[1,1])
    print(st)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"