class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV(Goods):
    pass
class Table(Goods):
    pass
class Notebook(Goods):
    pass
class Cup(Goods):
    pass

class Cart:
    def __init__(self, goods=[]):
        self.goods = goods[:]

    def add(self, gd):
        # добавление товара в корзину, представленного объектом gd;
        self.goods += [gd]
    
    def remove(self, indx):
        # удаление товара из корзины по индексу indx;
        self.goods.pop(indx)

    def get_list(self):
        # - получение товаров корзины в виде списка из строк:
        return [f'{i.name}: {i.price}' for i in self.goods]

cart = Cart()
tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)

print(*cart.get_list())