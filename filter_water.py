import time

class Filter:
    __date = None

    def __init__(self, date):
        if type(date) in {int, float} and date > 0:
            self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        return

class Mechanical(Filter):
    pass

class Aragon(Filter):
    pass

class Calcium(Filter):
    pass

class GeyserClassic:
    MAX_DATE_FILTER = 100
    filters_order = (Mechanical, Aragon, Calcium)
    slots = {1,2,3}
    filters = [None, None, None]

    def __init__(self):
        pass

    def add_filter(self, slot, filter:object):
        if slot in self.slots and self.filters[slot-1] == None and type(filter) == self.filters_order[slot-1]:
            self.filters[slot-1] = filter

    def get_filters(self):
        return tuple(self.filters)

    def water_on(self):
        t = time.time()
        if None in self.filters:
            return False

        if False in list(map(lambda x: 0 <= (t - x.date) <= self.MAX_DATE_FILTER, self.filters)):
            return False
        return True

    def remove_filter(self, slot):
        if slot in self.slots:
            self.filters[slot-1] = None


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"