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

class IntVal(Desc):
    #descriptor
    def __set__(self, instance, value):
        if type(value) is not int or value <= 0:
            TE()
        setattr(instance, self.name, value) 

class DictVal(Desc):
    #descriptor
    def __set__(self, instance, value):
        if type(value) is dict:
             if all(type(k) is str and type(v) in NUM for k, v in value.items()):
                setattr(instance, self.name, value)
                return 
        TE()       

class Aircraft:
    _model= StrVal()
    _mass = NumVal()
    _speed = NumVal()
    _top = NumVal()
    def __init__(self, model, mass, speed, top):
        self._model, self._mass, self._speed, self._top = model, mass, speed, top

    def __str__(self):
        return '\n'.join([f"{k}:{v}" for k, v in self.__dict__.items()])        

class PassengerAircraft(Aircraft):
    _chairs=IntVal()
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

class WarPlane(Aircraft):
    _weapons = DictVal()
    def __init__(self, name, mass, speed, top, weapons):
        super().__init__(name, mass, speed, top)
        self._weapons = weapons

#
planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

print(*planes)
try:
    a = Aircraft(54, 12, 300, 10000)
except TypeError:
    assert True
else:
    assert False, "Not generated exeption"

try:
    a = PassengerAircraft('model', 1, 2, 3, 1.2)
except TypeError:
    assert True
else:
    assert False, "Not generated exeption"
