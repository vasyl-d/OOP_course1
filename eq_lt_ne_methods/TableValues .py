class IntegerValue:
    #descriptor
    def __set_name__(self, owner, name):
        self.name = "__" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) is not int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value) 

class CellInteger:
    value = IntegerValue()
    def __init__(self, start_value:IntegerValue=0):
        self.value = start_value

    def __str__(self):
        return str(self.value)
    
    def __call__(self):
        return self.value

class TableValues:
    def __init__(self, rows:int, cols:int, cell=CellInteger):
        if not cell:
            raise ValueError('параметр cell не указан')
        if type(rows) is not int and type(cols) is not int:
            raise TypeError('rows and cols must be integers')
        self.rows, self.cols, self.cell = rows, cols, cell
        self.cells = tuple(tuple(self.cell() for r in range(self.cols)) for c in range(self.rows))
        
    def __getitem__(self, key):
        r, c = key
        if (type(r) is int and abs(r) < self.rows) and (type(c) is int and abs(c) < self.cols):
            return self.cells[r][c].value
        else:
            raise IndexError("Invalid cell index")

    def __setitem__(self, key, value):
        r, c = key
        if (type(r) is int and abs(r) < self.rows) and (type(c) is int and abs(c) < self.cols):
            self.cells[r][c].value = value
        else:
            raise IndexError("Invalid cell index")

    def __str__(self):
        return "\n".join([' '.join([str(c) for c in r]) for r in self.cells])

table = TableValues(2, 3, cell=CellInteger)
print(table)
print(table[0, 1])
table[1, 1] = 10
try:
    table[0, 0] = 1.45 # генерируется исключение ValueError
except ValueError:
    assert True
else:
    assert False, "Invalid values in table"

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()