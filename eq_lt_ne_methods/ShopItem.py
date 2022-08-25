import sys

class ShopItem:
    '''name - название товара (строка); weight - вес товара (число: целое или вещественное);
    s price - цена товара (число: целое или вещественное)'''
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        # - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
        return hash((self.name.lower(), self.weight, self.price))
        
    def __eq__(self, other):
        # - чтобы объекты с одинаковыми хэшами были равны.
        return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price

def str_dd (string):
    name, res = tuple(string.split(':'))
    weight, price = tuple(res.split())
    return (name, weight, price)

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
s = '''Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000'''
lst_in = [line for line in s.splitlines()]
shop_items = {ShopItem(*str_dd(line)): [ShopItem(*str_dd(line)), lst_in.count(line)] for line in lst_in}
print(shop_items)