class Exponat:
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

    def __setattr__(self, __name: str, __value) -> None:
        if type(__value) == str:
            object.__setattr__(self, __name, __value)
        else:
            raise TypeError("атрибуты -строки!")

'''p = Picture(название, художник, описание)         # локальные атрибуты: name - название; author - художник; descr - описание
m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание'''

class Picture(Exponat):
    def __init__(self, name, author, descr):
        self.author = author
        super().__init__(name, descr)

class Mummies(Exponat):
    def __init__(self, name,  location, descr):
        self.location = location
        super().__init__(name, descr)

class Papyri(Exponat):
    def __init__(self, name, date, descr):
        self.date = date
        super().__init__(name, descr)

class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        ''' - добавление нового экспоната в музей (в конец списка exhibits);'''
        self.exhibits.append(obj)


    def remove_exhibit(self, obj):
        ''' - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)'''
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        ''' - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).'''
        return (f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}")
               

mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)

mus.remove_exhibit(p)

for i, en in enumerate(mus.exhibits):
    print(mus.get_info_exhibit(i))