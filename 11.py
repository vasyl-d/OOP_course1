import sys

# здесь объявляются все необходимые классы
class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        if self.next_obj == None:
            self.next_obj = obj
        else:
            self.next_obj.link(obj)

    def get_data(self):
        print(self.data)
        if self.next_obj is not None: self.next_obj.get_data()


# считывание списка из входного потока (эту строку не менять)
#lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])

for i in lst_in[1:]:
    head_obj.link(ListObject(i)) 

#head_obj.get_data()

