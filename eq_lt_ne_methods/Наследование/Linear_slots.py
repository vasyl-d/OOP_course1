NUM = {int, float}

class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in NUM:
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    # здесь добавляйте еще один магический метод для умножения
    def __mul__(self, other):
        if type(other) not in NUM:
            raise TypeError('Амплитуда должно быть числом')

        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj

# здесь объявляйте класс Linear
class Linear(Function):
    __scope__ = '_k', '_b'

    def __init__(self, *args):
        super().__init__()
        if len(args) == 2:
            if all(type(x) in NUM for x in args):
                self._k, self._b = args
            else:
                raise TypeError('должны быть числа')
        elif len(args) == 1:
            obj = args[0]
            if type(obj) is __class__:
                self._k, self._b = obj._k, obj._b
            else:
                raise TypeError('Linear is expected')

    def _get_function(self, x):
        return self._k* x + self._b


f = Linear(1, 0.5)
f2 = f + 10   # изменение смещения (атрибут _bias)
y1 = f(0)     # 0.5
y2 = f2(0)    # 10.5
print(y1,y2)

f = Linear(1, 0.5)
f2 = f * 5    # изменение амплитуды (атрибут _amplitude)
y1 = f(0)     # 0.5
y2 = f2(0)    # 2.5
print(y1,y2)