class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.row = 0
        self.col = 0
        return self

    def __next__(self):
        if self.row >= len(self.lst):
            raise StopIteration
        try:
           r = self.lst[self.row][self.col]
        except Exception as e:
           raise IndexError(f"index out of range (выход индекса за допустимый диапазон), {e}")
        o = self.col
        self.col = self.col + 1 if self.col < self.row else 0
        self.row = self.row + 1 if self.row == o else self.row
        return r


lst = [[0],
       [10, 11],
       [20, 21, 22],
       [30, 31, 32, 33]]

it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)
