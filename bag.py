class StringValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) is str:
            setattr(instance, self.name, value)  
            

class WeightValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value:
            setattr(instance, self.name, value)  


class Thing:
    name = StringValue() # - наименование предмета;
    weight = WeightValue() #- вес предмета.

    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight

class Bag:
    max_weight = WeightValue()

    def __init__(self, max_weight = 1000) -> None:
        self.things = []
        self.max_weight = max_weight

    @property
    def things(self):
        return self.__things

    @things.setter
    def things(self, value):
        self.__things = value    

    def add_thing(self, thing:Thing): 
        # - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
        if self.get_total_weight()+thing.weight <= self.max_weight:
            self.things += [thing]

    def remove_thing(self, indx):
        # - удаление предмета по индексу списка __things;
        if indx < len(self.things):
            self.things.pop(indx)

    def get_total_weight(self):
        # - возвращает суммарный вес предметов в рюкзаке.
        w = 0
        for t in self.things:
            w += t.weight
        return w


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")