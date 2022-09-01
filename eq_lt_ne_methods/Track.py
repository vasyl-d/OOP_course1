from time import time
class Point:
    def __init__(self, x, y, speed):
        self.coord, self.speed = (x,y), speed

    def __call__(self):
        return self.coord, self.speed

class Track:
    def __init__(self, start_x, start_y):
        #start_x, start_y - start of route
        self.start_x, self.start_y, self.points = start_x, start_y, []

    def __getitem__(self, key):
        if type(key) is int and 0 <= key < len(self):
            return self.points[key]()
        raise IndexError(f'некорректный индекс, {key}')
    
    def __setitem__(self, key, value):
        if type(key) is int and 0 <= key < len(self) and type(value) in {int, float}:
            self.points[key].speed = value
        else:
            raise IndexError(f'некорректный индекс, {key}')

    def add_point(self, x, y, speed):
        # - добавление новой точки маршрута (линейный сегмент), который можно пройти со средней скоростью speed.
        self.points.append(Point(x, y, speed))

    def __len__(self):
        return len(self.points)

    def __str__(self) -> str:
        return '\n'.join([f"point:{el.coord}, speed:{el.speed}" for el in self.points])
t1 = time()
tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
print(tr)

tr[2] = 60
c, s = tr[2]
print(c, s)
try:
    res = tr[3] # IndexError
except IndexError:
    assert True
else:
    assert False, "must be an IndexError"
t2 = time()
print(t2-t1)

