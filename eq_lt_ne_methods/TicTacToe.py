from random import randint

NUM = {0, 1, 2}

class Cell:
    def __init__(self, value=0):
        self.__value = value
 
    @property
    def value(self): 
        return self.__value

    @value.setter
    def value(self, value=int):
        if value in NUM:
            self.__value = value
        else:
            raise ValueError("Value must be: 0 , 1 , 2 ")

    def __bool__(self):
        # true if value is 0 (empty)
        return self.value == 0  

class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple([tuple([Cell() for _ in NUM]) for __ in NUM])
    
    def init(self):
        for r in NUM:
            for  c in NUM:
                self.pole[r][c].value = self.FREE_CELL

    def chek_win(self, value):
        if_rows = any(all(map(lambda x: x.value == value, row)) for row in self.pole) #check all val in rows
        if_col = any(all(map(lambda x: x == value, (self.pole[r][c].value for r in {0,1,2}))) for c in {0,1,2}) #check all val in columns
        # chek diagonals
        if_fd = all(map(lambda x: x == value, (self.pole[c][c].value for c in {0,1,2}))) 
        if_sd = all(map(lambda x: x == value, (self.pole[r][-(r+1)].value for r in range(2,-1,-1))))
        return True if if_rows or if_col or if_fd or if_sd else False
      
    @property
    def is_human_win(self):
        #  - возвращает True, если победил human, иначе - False;
        return self.chek_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        #  - возвращает True, если победил компьютер, иначе - False;
        return self.chek_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        #  - возвращает True, если ничья, иначе - False.
        return True if not self.is_free_move() and not (self.is_computer_win or self.is_human_win) else False

    def __str__(self):
        return '\n'.join([' '.join([str(self.pole[r][c].value) for c in NUM]) for r in NUM])

    def show(self):
        return print(self)

    @staticmethod
    def IE():
        raise IndexError('некорректно указанные индексы')

    def chek_index(self, index):
        r, c = index
        return index if r in NUM and c in NUM else self.IE()

    def __getitem__(self, index):
        r, c = self.chek_index(index)
        return self.pole[r][c].value

    def __setitem__(self, index, value):
        r, c = self.chek_index(index)
        self.pole[r][c].value = value

    def is_free_move(self):
        # true if any free cell on pole
        return any(any(map(bool, row)) for row in self.pole)

    def __bool__(self):
        # true if any free cell and noone wins 
        return self.is_free_move() and not (self.is_human_win or self.is_computer_win)

    def human_go(self):
        #  - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
        r, c = tuple(map(int, input("Make your turn, please input 2 coords diveded by comma :").split(',')))
        while True:
            if r not in NUM or c not in NUM:
                r, c = tuple(map(int, input("try again, please input 2 coords {0,1,2} diveded by comma :").split(',')))
            else:
                if not self.pole[r][c]:
                    r, c = tuple(map(int, input("try again, please input 2 coords {0,1,2} diveded by comma of free Cell :").split(',')))
                else:
                    break
        self.pole[r][c].value = self.HUMAN_X

    def computer_go(self):
        #  - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).
        r, c = randint(0, 2), randint(0, 2)
        while not self.pole[r][c] and self.is_free_move():
            r, c = randint(0, 2), randint(0, 2)
        self.pole[r][c].value = self.COMPUTER_O

# game process

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

# tests
cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"