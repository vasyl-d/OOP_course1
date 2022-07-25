class Shop:
    def __init__(self, name:str=''):
        self.name = name
        self.goods = []

    def add_product(self, product):
        ''' - добавление нового товара в магазин (в конец списка goods);'''
        self.goods.append(product)

    def remove_product(self, product):
        ''' - удаление товара product из магазина (из списка goods);'''
        if product in self.goods:
            self.goods.remove(product)


class Product:
    index = 0
    
    def __init__(self, name:str, weight:str, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.__dict__['id'] = self.__get_index() + 1
        self.__set_index(self.id)

    @classmethod
    def __get_index(cls):
        return cls.index
    
    @classmethod
    def __set_index(cls, index):
        cls.index = index
    
    def __setattr__(self, __name, __value):
        if (__name in {'weight','price'} and type(__value) not in {float, int}) or (__name == 'name' and type(__value) != str) or (__name in {'weight','price'} and __value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        if __name != 'id':
            object.__setattr__(self, __name, __value)

    
    def __delattr__(self, __name: str) -> None:
        if __name =='id':
            raise AttributeError("Атрибут id удалять запрещено.")


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

assert shop.goods[0].id == 1, "не верный индекс у первого товара"

try:
    shop.add_product(Product("sfdg", -1, -1))
except TypeError:
    pass
assert True, "price, weight > = 0"