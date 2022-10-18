NUM = {int, float}

def TE(msg="wrong type"):
    raise TypeError(msg)

class Desc:
    #descriptor
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 

class NumVal(Desc):
    #descriptor
    def __init__(self, msg=""):
        self.msg = msg

    def __set__(self, instance, value):
        if type(value) not in NUM:
            TE(self.msg)
        setattr(instance, self.name, value)

class PointTrack:
    x = NumVal(msg='координаты должны быть числами')
    y = NumVal(msg='координаты должны быть числами')
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"

class Track:
    __points = []
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            if all([type(x) in NUM for x in args]):
                self.__points.append(PointTrack(args[0], args[1]))
        if all([type(x) is PointTrack for x in args]):
            self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)
    
    @points.setter
    def points(self, value):
        if type(value) is tuple:
            if all(type(x) is PointTrack for x in value):
                self.__points = value

    def add_back(self, pt):
        #  - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
        self.__points.append(pt)
    def add_front(self, pt):
        #  - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
        self.__points = pt + self.__points
    def pop_back(self):
        #  - удаление последней точки из маршрута;
        if self.__points:
            self.__points.pop()
    def pop_front(self):
        #  - удаление первой точки из маршрута.
        if self.__points:
            self.__points.pop(0)

# 

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)