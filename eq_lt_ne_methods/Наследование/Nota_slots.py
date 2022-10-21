NOTES = {'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'}
TON = {-1, 0, 1}

def VE():
    raise ValueError('недопустимое значение аргумента')

def IE():
    raise IndexError('недопустимый индекс')

class Note:
    __slots__ = '_name','_ton' 

    def __init__(self, name, ton):
        self._name, self._ton = name, ton

    def __setattr__(self, name, value):
        if (name == '_name' and value in NOTES) or (name == '_ton' and value in TON):
            super().__setattr__(name, value)
        else:
            VE()

class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    ID = None

    def __new__(cls, *args, **kwargs):
        cls.ID = cls.ID if cls.ID else super().__new__(cls)
        return cls.ID

    def __del__(self):
        __class__.ID = None

    def __init__(self):
        self._do = Note('до',0) 
        self._re = Note('ре',0)
        self._mi = Note('ми',0)
        self._fa = Note('фа',0)
        self._solt = Note('соль',0)
        self._la = Note('ля',0)
        self._si = Note('си',0)

    def __getitem__(self, key):
        return self.__getattribute__(self.__slots__[key]) if key in range(0,7) else IE()

    def __iter__(self):
        for key in self.__slots__:
            yield self.__getattribute__(key)


notes  = Notes()
print(notes._do._name, notes._do._ton)
print(notes[2]._name)
for i in notes:
    print(i._name, i._ton)

try:
    notes[3]._ton = 2
except ValueError:
    assert True
else:
    assert False, 'must be valid tone'

try:
    notes[3]._name = 2
except ValueError:
    assert True
else:
    assert False, 'must be valid tone'

try:
    notes[7]._ton = -1
except IndexError:
    assert True
else:
    assert False, 'must be valid index'

notes[0]._ton = -1
assert notes[0]._ton == -1 , 'не верно сработало присвоение'

for i in notes:
    print(i._name, i._ton)
