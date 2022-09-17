NUM = {int, float}

class Matrix:
    @classmethod
    def check_list(self, in_lst):
        l = len(in_lst[0])
        if all(len(row)==l for row in in_lst):
            if all((all(map(lambda el: type(el) in NUM, row)) for row in in_lst)):
                return in_lst
        raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and type(args[0]) is list:
            self.matrix = self.check_list(args[0])
        elif len(args) == 3:
            r, c, fill_value = args
            if type(r) is int and type(c) is int and r >= 0 and c >= 0 and type(fill_value) in NUM:
                self.matrix = [[fill_value for _ in range(c)] for _ in range(c)]
            else:
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __lenght(self):
        return (len(self.matrix), len(self.matrix[0]))

    @staticmethod
    def TE():
        raise TypeError('значения матрицы должны быть числами')

    @staticmethod
    def IE():
        raise IndexError('недопустимые значения индексов')

    def check_index(self, index): 
        r,c = index
        if type(r) is int and type(c) is int:
            lr, lc = self.__lenght()
            return (r, c) if 0 <= r < lr and 0 <= c < lc else self.IE()
        self.IE()

    def check_value(self, value):
        return value if type(value) in NUM else self.TE()

    def __getitem__(self, key):
        r, c = self.check_index(key)
        return self.matrix[r][c]

    def __setitem__(self, key, value):
        r, c = self.check_index(key)
        value = self.check_value(value)
        self.matrix[r][c] = value

    def __add__(self, other):
        r, c = self.__lenght()
        if type(other) == type(self) and other.__lenght() == (r, c):
            self.check_list(other.matrix)
            return Matrix([list(map(sum, zip(self.matrix[row], other.matrix[row]))) for row in range(r)])
        if type(other) in NUM:
            return Matrix([list(map(lambda x: x + other, self.matrix[row])) for row in range(r)])
        raise ValueError('операции возможны только с матрицами равных размеров')

    def __sub__(self, other):
        r,c = self.__lenght()
        if type(other) == type(self) and other.__lenght() == (r, c):
            self.check_list(other.matrix)
            return Matrix([list(map(lambda x: x[0]-x[1], zip(self.matrix[row], other.matrix[row]))) for row in range(r)])
        if type(other) in NUM:
            return Matrix([list(map(lambda x: x - other, self.matrix[row])) for row in range(r)])
        raise ValueError('операции возможны только с матрицами равных размеров')
    
    def __str__(self):
        return '\n'.join([' '.join([str(x) for x in r]) for r in self.matrix])
# tests

list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]

try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
print(m1)
m2 = Matrix([[0, 1], [1, 0]])
print(m2)
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"