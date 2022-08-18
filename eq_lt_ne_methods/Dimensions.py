class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    # a, b, c - габаритные размеры
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if self.check_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, value):
        if self.check_value(value):
            self.__b = value
    
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, value):
        if self.check_value(value):
            self.__c = value
    
    @classmethod
    def check_value(cls, value):
        if type(value) in {int, float} and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION:
            return True
        return False

    def __len__(self):
        return self.a*self.b*self.c

    def __eq__(self, __o: object) -> bool:
        if type(__o) in {int, float}:
            if len(self) == __o:
                return True
        elif type(__o) is Dimensions:
            if len(self) == len(__o):
                return True
        return False

    def __lt__(self, __o: object) -> bool:
        if type(__o) in {int, float}:
            if len(self) < __o:
                return True
        elif type(__o) is Dimensions:
            if len(self) < len(__o):
                return True
        return False
    def __le__(self, __o: object) -> bool:
        if type(__o) in {int, float}:
            if len(self) <= __o:
                return True
        elif type(__o) is Dimensions:
            if len(self) <= len(__o):
                return True
        return False
        

class ShopItem:
    '''где name - название товара (строка); 
    price - цена товара (целое или вещественное число); 
    dim - габариты товара (объект класса Dimensions).'''
    def __init__(self, name, price, dim:Dimensions):
        self.name = name
        self.price = price
        self.dim = dim

    def __str__(self):
        return f"name: {self.name} price: {self.price} dim: {self.dim.a}*{self.dim.b}*{self.dim.c}"

trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
#[print(el) for el in lst_shop]
lst_shop_sorted = sorted(lst_shop, key=lambda x: len(x.dim))
#[print(el) for el in lst_shop_sorted]