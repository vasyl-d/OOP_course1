class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name, self._massa, self._temp = name, massa, temp

    def __str__(self):
        return "\n".join([f"{v}: {self.__getattribute__(v)}" for v in __class__.__slots__])

class StarType(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star, self._radius = type_star, radius

class WhiteDwarf(StarType):
    __slots__ = ('_type_star', '_radius')
    #  - белый карлик;

class YellowDwarf(StarType):
    #  - желтый карлик;
    __slots__ = ('_type_star', '_radius')

class RedGiant(StarType):
    #  - красный гигант;
    __slots__ = ('_type_star', '_radius')

class Pulsar(StarType):
    #  - пульсар.
    __slots__ = ('_type_star', '_radius')

stars = [
        RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
        WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
        WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
        YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)
        ]

white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))

print(*white_dwarfs)
print(len(white_dwarfs))

assert len(white_dwarfs) == 2, "функция filter вернула неверное количествло"

try:
    r = RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45)
    r.ss = 0
except AttributeError:
    assert True
else:
    assert False, "Must be Exeption on added new attribute"




