NUM = {int, float}

def TE(msg="type error"):
    raise TypeError(msg)

class Food:
    def __init__(self, name:str, weight, calories):
        self.name, self.weight, self.calories = name, weight, calories

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value if type(value) is str else TE("Must be string")
            
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        self._weight = value if type(value) in NUM and value > 0  else TE("Must be number greater than 0") 

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value if type(value) in NUM and value > 0 else TE("Must be number greater than 0")

    def __str__(self):
        return "\n".join([f"{k}: {v}, " for k, v in self.__dict__.items()])

class BreadFood(Food):
    def __init__(self, name, weight, calories, white=True):
        # white - True для белого хлеба, False - для остальных
        super().__init__(name, weight, calories)
        self._white = white
        
    @property
    def white(self):
        return self._white
    @white.setter
    def white(self, value):
        self._white = value if type(value) is bool else TE("Must be number greater than 0")

class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary=False): 
        # dietary - True для диетического супа, False - для других видов
        super().__init__(name, weight, calories)
        self._dietary = dietary

    @property
    def dietary(self):
        return self._dietary
    @dietary.setter
    def white(self, value):
        self._dietary = value if type(value) is bool else TE("Must be number greater than 0")

class FishFood(Food):
    def __init__(self, name, weight, calories, fish:str):
        # fish - вид рыбы (семга, окунь, сардина и т.д.)
        super().__init__(name, weight, calories)
        self._fish = fish

    @property
    def fish(self):
        return self._fish
    @fish.setter
    def fish(self, value):
        self._fish = value if type(value) is bool else TE("Must be number greater than 0")

if __name__ == "__main__":
    bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
    sf = SoupFood("Черепаший суп", 520, 890.5, False)
    ff = FishFood("Консерва рыбная", 340, 1200, "семга")
    print(bf, "\n ______")
    print(sf, "\n______")
    print(ff, )

    #tests
