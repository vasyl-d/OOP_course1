class Thing:
    #name - название предмета (строка); mass - масса предмета (число: целое или вещественное)
    def __init__(self, name:str, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, __o: object) -> bool:
        if type(__o) is Thing:
            return True if self.name.lower() == __o.name.lower() and self.mass == __o.mass else False
        return False

    def __lt__(self, __o: object) -> bool:
        if type(__o) is Thing:
            return True if self.name.lower() < __o.name.lower() or self.mass < __o.mass else False
        return False

class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        # - добавление предмета obj (объект другого класса Thing) в ящик;
        self.things.append(obj)
    def get_things(self):
        # - получение списка объектов ящика.
        return self.things
    def __eq__(self, __o: object) -> bool:
        return sorted(self.get_things()) == sorted(__o.get_things())

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)