class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        setattr(instance, self.name, value)
    
    @staticmethod
    def isfloat(self, value):
        if type(value) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")        

class Cell:
    value = FloatValue()

    def __init__(self, value) -> None:
        self.value = value

class TableSheet:
        
        def __init__(self) -> None:
            pass

N = 2
M = 3
table = TableSheet(N, M)
assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"