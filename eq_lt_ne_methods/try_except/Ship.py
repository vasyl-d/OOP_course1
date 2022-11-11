from random import randint

class Ship:
    __slots__ = ('_length', '_tp', '_x', '_y','_is_move', '_cells')
    def __init__(self, length, tp=1, x=None, y=None) -> None:
        self._cells = [1]*self._length

    @property
    def _is_move(self):
        return all(self._cells)

    def set_start_coords(x, y):
        ''' - установка начальных координат (запись значений в локальные атрибуты _x, _y);'''
        pass
    def get_start_coords():
        ''' - получение начальных координат корабля в виде кортежа x, y;'''
        pass
    def move(go):
        ''' - перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True;'''
        pass
    def is_collide(ship):
        ''' - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение есть и False - в противном случае;'''
        pass
    def is_out_pole(size):
        ''' - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;'''
        pass

    def __getitem__(self, key):
        return self._cells[key]

    def __setitem__(self, key, value):
        self._cells[key] = value
        

class GamePole:
    __slots__ = '_size','_ships'
    def __init__(self, size=10) -> None:
        self._size, self._ships = size, []

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), 
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

    def get_ships():
        ''' - возвращает коллекцию _ships;'''
        pass
    def move_ships():
        ''' - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;'''
        pass
    def show():
        ''' - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);'''
        pass

    def get_pole():
        ''' - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.'''
        pass
# 

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()

