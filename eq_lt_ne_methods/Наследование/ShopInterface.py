NUM = {int, float}

def TE():
    raise TypeError('неверный тип аргумента')

class Desc:
    #descriptor
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 

class StrVal(Desc):
    def __set__(self, instance, value):
        if type(value) is not str:
            TE()
        setattr(instance, self.name, value) 

class NumVal(Desc):
    #descriptor
    def __set__(self, instance, value):
        if type(value) not in NUM or value < 0:
            TE()
        setattr(instance, self.name, value) 

class ShopInterface:

    def get_id(self):
        raise NotImplementedError("в классе не переопределен метод get_id")

class ShopItem(ShopInterface):
    ID = 0
    _name = StrVal()
    _weight = NumVal()
    _price = NumVal()

    def __init__(self, name, weight, price):
        self.__id = __class__.ID
        __class__.ID += 1
        self._name, self._weight, self._price = name, weight, price

    def get_id (self):
        return self.__id

item1 = ShopItem("имя1", 1, 100)
item2 = ShopItem("имя2", 2, 200)
print(item1.get_id())
print(item2.get_id())
