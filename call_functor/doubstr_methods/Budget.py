NUM = {int, float}

class Item:
    ''' name - название статьи расхода; money - сумма расходов (вещественное или целое число)'''
    def __init__(self, name:str, money:float):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        if type(other) in NUM:
            return self.money + other
    
    def __radd__(self, other):
        return self.__add__(other)

class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        # - добавление статьи расхода в бюджет (it - объект класса Item);
        if isinstance(it, Item):
            self.items.append(it)

    def remove_item(self, indx):
        # - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
        if type(indx) == int and 0 <= indx <= len(self.items):
            self.items.pop(indx)

    def get_items(self):
        # - возвращает список всех статей расходов (список из объектов класса Item).
        return self.items

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    print(x.money)
    s += x
print('Total: %d' % s)

