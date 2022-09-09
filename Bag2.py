from math import isclose
# make additions for float comparisons

class StringValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) is str:
            setattr(instance, self.name, value) 
        else:
            raise TypeError("Must be string") 
            

class WeightValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value:
            setattr(instance, self.name, value) 
        else:
            raise TypeError("Weight must be int or float") 


class Thing:
    name = StringValue() # - наименование предмета;
    weight = WeightValue() #- вес предмета.

    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.weight + other.weight
        elif isinstance(other, (int, float)):
            return self.weight + other
        else:
            raise TypeError("Weight must be int or float")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.weight - other.weight
        elif isinstance(other, (int, float)):
            return self.weight - other
        else:
            raise TypeError("Weight must be int or float") 

    def __rsub__(self, other):
        if isinstance(other, self.__class__):
            return other.weight - self.weight
        elif isinstance(other, (int, float)):
            return other - self.weight
        else:
            raise TypeError("Weight must be int or float") 

    def __str__(self) -> str:
        return f"{self.name}: {self.weight}"     

class Bag:
    max_weight = WeightValue()

    def __init__(self, max_weight = 1000) -> None:
        self.things = []
        self.max_weight = max_weight

    @property
    def things(self):
        return self.__things

    @things.setter
    def things(self, value):
        self.__things = value    

    @staticmethod
    def IE():
        raise IndexError('неверный индекс')
    @staticmethod
    def VE():
        raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing:Thing): 
        # - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
        if self.weight() + thing.weight <= self.max_weight or isclose(self.weight() + thing.weight, self.max_weight):
            self.things += [thing]
        else:
            self.VE()

    def remove_thing(self, indx):
        # - удаление предмета по индексу списка __things;
        if indx < len(self.things):
            self.things.pop(indx)

    def weight(self):
        # - возвращает суммарный вес предметов в рюкзаке.
        return sum(self.things)
    
    def __getitem__(self, key):
        return self.things[key] if type(key) is int and key < len(self.things) else self.IE()

    def __setitem__(self, key, value):
        if type(key) is int and key < len(self.things):
            if (self.weight() + value - self.things[key] <= self.max_weight) or isclose(self.weight() + value - self.things[key], self.max_weight):
                self.things[key] = value
            else:
                self.VE()
        else:
            self.IE()

    def __delitem__(self, key):
        return self.things.pop(key) if type(key) is int and key < len(self.things) else self.IE()

    def __str__(self) -> str:
        return "\n".join([f"{t.name}: {t.weight}" for t in self.things])

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.weight()
print(bag)
print(w)


#проверки
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)
print(b)
try:
    b[0] = Thing('рубашка', 800)
    print(b)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"

bag = Bag(0.3)
bag.add_thing(Thing('книга', 0.2))
bag.add_thing(Thing('носки', 0.1)) #для флоат надо использовать math.isclose()