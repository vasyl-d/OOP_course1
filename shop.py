class StringValue:
    def __init__(self, min_lenght=2, max_lenght=50) -> None:
        self.max_lenght = max_lenght
        self.min_lenght = min_lenght

    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) is str and self.min_lenght <= len(value) <= self.max_lenght:
            setattr(instance, self.name, value)  
            

class PriceValue:
    def __init__(self, max_value=10000) -> None:
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)  
            

class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name:str, goods:list=[]) -> None:
        self.name = name # - название магазина (строка);
        self.goods = goods #- список из товаров.
        
    def add_product(self, product:Product): # - добавление товара в магазин (в конец списка goods);
        self.goods += [product]

    def remove_product(self, product:Product): # - удаление товара из магазина (из списка goods).
        if self.goods.index(product):
            self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))

for p in shop.goods:
    print(f"{p.name}: {p.price}")
    

assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"

t = Product("name 123", 1000)
shop.add_product(t)
shop.remove_product(t)
assert len(shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')

t = Product(1000, "name 123")
if hasattr(t, '_name'):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, '_price'):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"