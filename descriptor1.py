class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)
    
    

class Cell:
    value = FloatValue()

    def __init__(self, value = 0.0) -> None:
        self.value = value
    

class TableSheet:
        
        def __init__(self, n, m) -> None:
            self.n = n
            self.m = m
            self.cells = [[Cell() for i in range(m)] for j in range(n)] 
        
        def prn(self):
            #[[print(self.cells[i][j].value, ['', '\n'][(i+1)//len(self.cells)], sep=' ', end='') for i in range(len(self.cells))] for j in range(len(self.cells[0]))]
            for i in range(len(table.cells)):
                for j in range(len(table.cells[0])):
                    print(table.cells[i][j].value,'  ', end='')
                print('\n')

N = 5
M = 3
table = TableSheet(N, M)
#от 1.0 до 15.0
z = 1.0
for i in range(len(table.cells)):
    for j in range(len(table.cells[0])):
        table.cells[i][j].value=z
        z += 1.0

assert len(table.cells[0]) == 3 and len(table.cells) == 5, 'Wrong len'
table.prn()

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"