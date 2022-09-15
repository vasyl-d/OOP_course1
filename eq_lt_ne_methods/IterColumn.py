class IterColumn:
    def __init__(self, lst, column):
        self.lst, self.column = lst, column
        if type(column) is not int and column >= len(lst[0]):
            raise IndexError("Index out of range")

    def __iter__(self):
        for el in self.lst:
            yield el[self.column]

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)