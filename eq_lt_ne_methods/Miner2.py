from random import randint

class Cell:
    '''__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
        __number - число мин вокруг клетки (целое число от 0 до 8);
        __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.'''
    def __init__(self, is_mine:bool=False, number:int=0, is_open:bool=False):
            self.is_mine = is_mine
            self.number = number
            self.is_open = is_open
 
    def __bool__(self):
        return not self.is_mine
    
    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) is bool:
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) is bool:
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) is int and 0 <= value <= 8:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __str__(self):
        s = "🍀"
        if self.is_open:
            s = "😱" if self.is_mine else "🍥"
        return s

class GamePole:
    #singletom
    __pole_cells: list = []
    __instance_id = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance_id is None:
            cls.__instance_id = super().__new__(cls)
        return cls.__instance_id

    def __init__(self, N:int=2, M:int=2, total_mines:int=2):
        if type(N) is int and type(M) is int and type(total_mines) is int and 0 <= N and 0 < M and 0 < total_mines < M*N:
            self.rows = N
            self.cols = M
            self.total_mines = total_mines
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def pole(self):
        return self.__pole_cells

    @pole.setter
    def pole(self, value):
        #pole - readonly property
        pass

    def init_pole(self):
        # - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
        #создаем набор координат мин
        self.minerows = set()
        while len(self.minerows) < self.total_mines:
            x = randint(0,self.rows - 1)
            y = randint(0,self.cols - 1)
            self.minerows.add((x, y))
        #создаем двумерный список - поле и расставляем мины
        self.__pole_cells = [[Cell(is_mine=True, number=self._count_mines(r,c)) if (r,c) in self.minerows else Cell(is_mine=False, number=self._count_mines(r,c)) for c in range(self.cols) ] for r in range(self.rows)]


    def _count_mines(self, x, y):
        min_r = 0 if x <= 0 else x-1
        max_r = x + 2 if x < self.rows else x
        min_c = 0 if y <= 0 else y-1
        max_c = y + 2 if y < self.cols else y
        return sum([1 if (r, c) in self.minerows else 0 for c in range(min_c, max_c) for r in range(min_r, max_r)])       
        
    def open_cell(self, i, j):
        # - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута 
        # __is_open объекта Cell в ячейке (i, j) на True;
        if (0 <= i < self.rows) and (0 <= j < self.cols):
            self.__pole_cells[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        # - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).
        [print(r[c],('\n' if c == self.cols-1 else ' '), end='', sep='')  for r in self.__pole_cells for c in range(self.cols)]

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
print("before")
pole.show_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
print("after:")
pole.show_pole()

#tests

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k+i, l+j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1
                
    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"