class Thing:
    def __init__(self, name, price, weight):
        self.name, self.price, self.weight = name, price, weight

    def __hash__(self) -> int:
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def check_key(self, key):
        if isinstance(key, Thing):
            return True
        else:
            raise TypeError('ключами могут быть только объекты класса Thing')
        
    def __init__(self, in_dict = {}):
        if isinstance(in_dict, dict):
            if all(self.check_key(x) for x in in_dict.keys()):
                super().__init__(in_dict)
        else:
            raise TypeError('аргумент должен быть словарем')

    def __setitem__(self, key, value) -> None:
        if self.check_key(key):
            return super().__setitem__(key, value)
            

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)
print(th_1 == th_2)

try:
    dict_things[1] = th_1 # исключение TypeError
except TypeError:
    assert True
else:
    assert False, "TypeError expected"

things = {}
things['1'] = th_1

try:
    dict_things = DictShop(things)# исключение TypeError
except TypeError:
    assert True
else:
    assert False, "TypeError expected"

dict_things = DictShop(['2',2])