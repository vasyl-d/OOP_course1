class CellException(Exception):
    def __str__(self):
        return "значение выходит за допустимый диапазон"

class CellIntegerException(CellException):
    pass
class CellFloatException(CellException):
    pass
class CellStringException(CellException):
    def __str__(self):
        return "длина строки выходит за допустимый диапазон"

class Cell:
    __slots__ = '_min_value', '_max_value', '_value', '_type', '_exc'
    def __init__(self, min_value, max_value) -> None:
        self._min_value, self._max_value, self._value = min_value, max_value, None
        self._type = {int, float, str}
        self._exc = CellException()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        t = type(value)
        if t in self._type:
            if (t in {int, float} and self._min_value <= value <= self._max_value) or (t is str and self._min_value <= len(value)<= self._max_value):
                self._value = value
            else:
                raise self._exc

    def __call__(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)

class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self._type = {int}
        self._exc = CellIntegerException()

class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self._type = {float}
        self._exc = CellFloatException()

class CellString(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self._type = {str}
        self._exc = CellStringException()

class TupleData():
    
    def __init__(self, *args):
        if any(not isinstance(x, Cell) for x in args):
            raise TypeError("Must be an iterable with Cell classes in it")
        self.tpl = args if args else tuple()

    def __len__(self) -> int:
        return len(self.tpl)

    def __iter__(self):
        for el in self.tpl:
            yield el.value

    def __getitem__(self, key):
        return self.tpl[key].value

    def __setitem__(self, key, value):
        self.tpl[key].value = value

# 
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"

except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception as e:
    print("Общая ошибка при работе с объектом TupleData". e)

res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)

# 
t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]

for i, x in enumerate(t):
     print(i, x)
     assert x == d[i], f"объект класса TupleData хранит неверную информацию x = {x} {type(x.value)}, d[i] = {d[i]} {type(d[i])}"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"


cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

    
cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

    
cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(CellStringException, CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"