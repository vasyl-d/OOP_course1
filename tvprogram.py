class Telecast:
    __id = 0
    __name = ''
    __duration = 0

    def __init__(self, uid:int, name:str, duration:int) -> None:
        self.uid = uid
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return self.__id
    @uid.setter
    def uid(self, uid):
        self.__id = uid 

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name 

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = duration


class TVProgram:
    def __init__(self, name) -> None:
        self.items=[]
        self.name = name

    def add_telecast(self, tl:Telecast): 
        # - добавление новой телепередачи в список items;
        self.items += [tl]

    def remove_telecast(self, indx):
        # - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).
       i = self.find_tl(indx)
       if i != None:
            self.items.pop(i)

    def find_tl(self, indx):
        res = None
        for i, el in enumerate(self.items):
            if el.uid == indx:
                res = i
                break
        return res

    def prn(self):
        for t in self.items:
            print(f"{t.uid}: {t.name}: {t.duration}")


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.prn()
pr.remove_telecast(2)
pr.prn()


assert hasattr(TVProgram, 'add_telecast') and hasattr(TVProgram, 'remove_telecast'), "в классе TVProgram должны быть методы add_telecast и remove_telecast"

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Новости", 2000))
t = Telecast(2, "Интервью с Балакиревым", 20)
pr.add_telecast(t)

pr.remove_telecast(3)
assert len(pr.items) == 2, "неверное число телеперач, возможно, некорректно работает метод remove_telecast"
assert pr.items[-1] == t, "удалена неверная телепередача (возможно, вы удаляете не по __id, а по порядковому индексу в списке items)"

assert type(Telecast.uid) == property and type(Telecast.name) == property and type(Telecast.duration) == property, "в классе Telecast должны быть объекты-свойства uid, name и duration"

for x in pr.items:
    assert hasattr(x, 'uid') and hasattr(x, 'name') and hasattr(x, 'duration')

assert pr.items[0].name == "Доброе утро", "объект-свойство name вернуло неверное значение"
assert pr.items[0].duration == 10000, "объект-свойство duration вернуло неверное значение"

t = Telecast(1, "Доброе утро", 10000)
t.uid = 2
t.name = "hello"
t.duration = 10