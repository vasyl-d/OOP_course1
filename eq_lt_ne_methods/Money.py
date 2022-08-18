class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    
    def __init__(self):
        return None
    @classmethod
    def register(cls, money):
        money.cb = cls

class Money:
    def __init__(self, volume=0, cb:CentralBank=None):
        self.__volume = volume
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, money):
        self.__volume = money

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def get_kval(self):
        if self.cb != None:
            if self.name in self.cb.rates:
                 return round(self.volume/self.cb.rates[self.name],1) 
        raise ValueError("Неизвестен курс валют.")      

    def __eq__(self, other):
        return True if self.get_kval() == other.get_kval() else False

    def __gt__(self, other):
        return True if self.get_kval() > other.get_kval() else False

    def __ge__(self, other):
        return True if self.get_kval() >= other.get_kval() else False 

class MoneyR(Money):
    name = "rub"
class MoneyD(Money):
    name = "dollar"
class MoneyE(Money):
    name = "euro"

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 0.985}

r = MoneyR(45000)
d = MoneyD(500)
e = MoneyE(200)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")