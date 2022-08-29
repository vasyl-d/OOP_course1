import random

class Cell:
    def __init__(self, r, c, mine=False, around_mines=0):
        self.init(r, c, mine, around_mines)

    def init(self, r, c, mine=False, around_mines=0):
        self.row = r
        self.col = c
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False
    def show(self):
        dp = '#'
        if self.fl_open:
            if self.mine:
                dp = '*'
            else:
                dp = self.around_mines
        return dp
    def show_(self):
        return '*' if self.mine else self.around_mines

class GamePole:
    def __init__(self, N, M):
        self.rows = N
        self.cols = M
        self.pole = []
 
        #создаем набор координат мин
        self.minerows = set()
        while len(self.minerows) < M:
            x = random.randint(0,self.rows - 1)
            y = random.randint(0,self.cols - 1)
            self.minerows.add((x,y))

        #создаем двумерный список - поле и расставляем мины
        self.pole = [[Cell(r, c, mine=True) if (r,c) in self.minerows else Cell(r, c, mine=False, around_mines=self._count_mines(r,c)) for c in range(self.cols) ] for r in range(self.rows)]

        #надо просчитать сколько мин вокруг для свободных ячеек
    def _count_mines(self, x, y):
        min_r = 0 if x <= 0 else x-1
        max_r = x + 2 if x < self.rows else x
        min_c = 0 if y <= 0 else y-1
        max_c = y + 2 if y < self.cols else y
        l1 = [1 if (r, c) in self.minerows else 0 for c in range(min_c, max_c) for r in range(min_r, max_r)]       
        return sum(l1)

    def show(self):
        [print(r[c].show(),('\n' if c == self.cols-1 else ' '), end='', sep='')  for r in self.pole for c in range(self.cols)]

    def show_(self):
        [print(r[c].show_(),('\n' if c == self.cols-1 else ' '), end='', sep='')  for r in self.pole for c in range(self.cols)]


gp = GamePole(10,12)
gp.pole[3][3].fl_open = True
gp.pole[1][2].fl_open = True
gp.show()
print('------------')
gp.show_()
print(*gp.minerows)