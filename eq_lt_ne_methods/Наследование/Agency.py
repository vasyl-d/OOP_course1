class SellItem:
    def __init__(self, name:str, price:float):
        self.name, self.price = name, price

    def __hash__(self) -> int:
        return hash((self.name, self.price))

class Flat(SellItem):
    def __init__(self, name:str, price:float, size:int, rooms:int):
        super().__init__(name, price)
        self.size, self.rooms = size, rooms

class House(SellItem):
    def __init__(self, name:str, price:float, material:str, square:float):
        super().__init__(name, price)
        self.material, self.square = material, square

class Land(SellItem):
    def __init__(self, name:str, price:float, square:float):
        super().__init__(name, price)
        self.square = square

# class Agency(list):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name

#     def add_object(self, obj):
#         self.append(obj)

#     def remove(self, obj):
#         if obj in self:
#             self.remove(obj)

#     def get_objects(self):
#         return self

class Agency:
    def __init__(self, name:str):
        self.name = name
        self.__listing = dict()

    def add_object(self, obj):
        #  - добавление нового объекта недвижимости для продажи (один из объектов классов: House, Flat, Land);
        if issubclass(obj.__class__, SellItem):
            self.__listing[obj] = obj

    def remove_object(self, obj):
        #  - удаление объекта obj из списка объектов для продажи;
        if issubclass(obj.__class__, SellItem) and obj in self.__listing:
            self.__listing.pop(obj)

    def get_objects(self):
        #  - возвращает список из всех объектов для продажи.
        return self.__listing.values()

    def __iter__(self):
        for value in self.__listing.values():
            yield value

ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов