class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__check_value(value):
            self.__x = value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__check_value(value):
            self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if self.__check_value(value):
            self.__radius = value

    @classmethod
    def __check_value(cls, value):
        if type(value) not in {int, float}:
            return False
        return True
            
    def __getattr__(self, __name: str):
        return False


    def __setattr__(self, key, value):
        if type(value) not in (float, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value < 0:
            value = self.__radius

        super().__setattr__(key, value)

    '''def __setattr__(self, __name: str, __value):
        xx = {'_Circle__x', '_Circle__y'}
        rr = {'_Circle__radius'}

        if '_Circle_' in __name:         
            if (__name in xx and type(__value) in {int, float}) or (__name in rr and type(__value) in {int, float} and __value >=0) :
                object.__setattr__(self, __name, __value)
            elif __name in self.__dict__:
                return
            else:
                raise TypeError(f"Invalid attribute: {__name} {__value}")
        elif (__name in {'x','y'} and type(__value) in {int, float}) or (__name =='radius' and type(__value) in {int, float} or __value >= 0):
            object.__setattr__(self, __name, __value)'''


circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует

assert type(Circle.x) == property and type(Circle.y) == property and type(Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, '7', 22)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(20, 7, 22)
assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = '20'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

'''Но надо было так:

class Circle:

    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x (self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def __setattr__(self, key, value):
        if type(value) not in (float, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value < 0:
            value = self.__radius

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False
'''