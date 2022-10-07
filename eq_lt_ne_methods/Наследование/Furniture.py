class Furniture:
    def __init__(self, name:str, weight:float):
        self._name, self._weight = name, weight

    @staticmethod
    def TE(msg):
        raise TypeError(msg)

    def __verify_name(self, name):
        #  - для проверки корректности имени;
        return name if type(name) is str else self.TE("название должно быть строкой")

    def __verify_weight(self, weight):
        return weight if type(weight) in {int, float} else self.TE("вес должен быть положительным числом")


    @property
    def _name(self):
        return self.__name
    
    @_name.setter
    def _name(self, value):
        self.__name = self.__verify_name(value)

    @property
    def _weight(self):
        return self.__weight
    
    @_weight.setter
    def _weight(self, value):
        self.__weight = self.__verify_weight(value)

    def get_attrs(self):
        return tuple(self.__dict__.get(x) for x in self.__dict__.keys() if x[0] == '_' and x[1] != '_')

class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
           # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей (целое число)
        super().__init__(name, weight)
        self._tp, self._doors = tp, doors

class Chair(Furniture):
    def __init__(self, name, weight, height):
        # height - высота стула (любое положительное число)
      super().__init__(name, weight)
      self._height = height

class Table(Furniture):
    def __init__(self,name, weight, height, square):
         # height - высота стола; square - площадь поверхности (любые положительные числа)
        super().__init__(name, weight)
        self._height, self._square = height, square

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())

    