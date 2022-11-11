class Thing:
    __slots__ = 'name','weight'
    def __init__(self, name, weight) -> None:
        self.name, self.weight = name, weight

class Box:
    '''_name - ссылка на параметр name;
    _max_weight - ссылка на параметр max_weight;
    _things - список из вещей, хранящиеся в ящике (изначально пустой список).'''
    __slots__ = ('_name', '_max_weight', '_things')
    def __init__(self, name=None, max_weight=0) -> None:
        self._name, self._max_weight, self._things = name, max_weight, []

    def add_thing(self, obj:tuple):
        name, weight = obj
        if weight + sum(x.weight for x in self._things) <=self._max_weight:
            self._things.append(Thing(name, weight))
        else:
            raise ValueError('превышен суммарный вес вещей')

    def __repr__(self):
        return f"{self._name} {self._max_weight}:\n" + '\n'.join(f"{x.name} {x.weight}" for x in self._things)

class BoxDefender:
    def __init__(self, box:Box) -> None:
        self.box = box
        self.newbox = Box(box._name, box._max_weight)
        self.newbox._things = box._things[:] 

    def __enter__(self):
        return self.newbox

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type == None:
            self.box._things = self.newbox._things[:]
        return False

box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

print(box)

try:
    with BoxDefender(box) as b:
        b.add_thing(("зонт", 346.6))
        b.add_thing(("шина", 500))
except ValueError:
    pass

print(box)

# tests

b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2
        
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"