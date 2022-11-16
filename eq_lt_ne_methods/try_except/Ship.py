from random import randint, randrange

SIZE_GAME_POLE = 10

class ShipException(Exception):
    pass

class OutOfPoleExeption(ShipException):
    pass

class CollideExeption(ShipException):
    pass

class Ship:
    __slots__ = ('_length', '_tp', '_x', '_y', '_cells', '_pole')
    def __init__(self, length, tp=1, x=None, y=None) -> None:
        self._length = length
        self._tp = tp
        self._cells = [1]*self._length
        self._x, self._y = x, y
        self._pole = None

    @property
    def _is_move(self):
        return sum(self._cells) == self._length

    @property
    def _height(self):
        return 1 if self._tp == 1 else self._length

    @property
    def _width(self):
        return self._length if self._tp == 1 else 1 

    def set_start_coords(self, x, y):
        ''' - установка начальных координат (запись значений в локальные атрибуты _x, _y);'''
        self._x, self._y = x, y

    def get_start_coords(self):
        ''' - получение начальных координат корабля в виде кортежа x, y;'''
        return (self._x, self._y)

    def move(self, go=1):
        ''' - перемещение корабля в направлении его ориентации на go клеток 
        (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку); 
        движение возможно только если флаг _is_move = True;'''
        if self._is_move:
            return False
        if self._pole == None:
            return False

        x, y = self.get_start_coords()
        if self._tp == 1:
            x = self._x + 1 if go else self._x - 1 
        else:
            y = self._y + 1 if go else self._y - 1 

        try:            
            new = Ship(self._length, self._tp, x, y)
            new._cells = self._cells[:]
            
            if new.is_out_pole(self._pole._size): #check bordercrossing
                raise OutOfPoleExeption
            if any(new.is_collide(el) for el in self._pole.get_ships() if el != self): # check if collide with others
                raise CollideExeption
            self.set_start_coords(x, y)
        except (OutOfPoleExeption, CollideExeption):
            return False
        finally:
            del new
        return True


    def is_collide(self, other):
        ''' - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение есть и False - в противном случае;'''
        # //two rectangles intersection
        # A.X1 < B.X2:	true
        # A.X2 > B.X1:	true
        # A.Y1 < B.Y2:	true
        # A.Y2 > B.Y1:	true
        # Intersect:	true
        if (self._x - 1 < other._x + other._width) and (self._x + self._width + 1 > other._x) and (self._y - 1 < other._y + other._height) and (self._y + self._height + 1 > other._y):
            return True
        else:
            return False
        
    def is_out_pole(self, size):
        ''' - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;'''
        if (self._tp == 1 and self._x + self._length > size) or (self._tp == 2 and self._y + self._length > size) or (self._x >= size or self._y >= size):
            return True
        return False

    def __getitem__(self, key):
        return self._cells[key]

    def __setitem__(self, key, value):
        self._cells[key] = value
        

class GamePole:
    __slots__ = '_size','_ships'
    def __init__(self, size=10) -> None:
        self._size, self._ships = size, None

    def init(self):
        self._ships = []
        temp_ships = [Ship(4, tp=randint(1, 2)), 
                            Ship(3, tp=randint(1, 2)), 
                            Ship(3, tp=randint(1, 2)), 
                                Ship(2, tp=randint(1, 2)),
                                Ship(2, tp=randint(1, 2)),
                                Ship(2, tp=randint(1, 2)),
                                    Ship(1  , tp=randint(1, 2)),
                                    Ship(1  , tp=randint(1, 2)),
                                    Ship(1  , tp=randint(1, 2)),
                                    Ship(1  , tp=randint(1, 2))
                        ]
        # make ships random positioning 
        # 
        for el in temp_ships:
            sd = Ship(el._length, el._tp)
            while True:               
                x = randint(0, self._size-1)
                y = randint(0, self._size-1)
                sd.set_start_coords(x, y)
                if not sd.is_out_pole(self._size):
                    if self._ships == []:
                        break
                    elif all(sd.is_collide(_) == False for _ in self._ships if _ != el):
                        break
            el._pole = self
            el.set_start_coords(x, y)
            self._ships.append(el)
            


    def get_ships(self):
        ''' - возвращает коллекцию _ships;'''
        return self._ships
        
    def move_ships(self):
        ''' - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) 
        в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля), 
        то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;'''
        free_ships = filter(lambda x: x._is_move, self._ships)
        for el in free_ships:
            go = randrange(-1,2,2)
            if not el.move(go):
                el.move(-go)
            
    def show(self):
        ''' - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);'''
        [print(*el) for el in self.get_pole()] 

    def get_pole(self):
        ''' - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.'''
        pole = [[0]*self._size for _ in range(self._size)]
        for el in self.get_ships():
            x, y = el.get_start_coords()
            if el._tp == 1:
                for i, v in enumerate(el._cells):
                    pole[y][x+i] = v
            else:
                for i, v in enumerate(el._cells):
                    pole[y+i][x] = v
        return tuple(tuple(_) for _ in pole)

# 

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

print('___________')
print(pole.get_pole())

[print(f"Корабль: палуб: {x._length}, координаты: {x._x}, {x._y}, ориентация: {x._tp}") for x in pole._ships]

pole.move_ships()
print()
pole.show()

# tests

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

print(f"Корабль s1: tp: {s1._tp}, coord: {s1._x, s1._y} w:{s1._width}, h:{s1._height}")
print(f"Корабль s2: tp: {s2._tp}, coord: {s2._x, s2._y} w:{s2._width}, h:{s2._height}")
print(f"Корабль s3: tp: {s3._tp}, coord: {s3._x, s3._y} w:{s3._width}, h:{s3._height}")
print(s1.is_collide(s3))

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
print('test:')
p.show()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()
    
gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
pole_size_8.show()
