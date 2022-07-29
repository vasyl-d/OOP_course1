class LessonItem:
    attrs = {'practices':int, 'duration':int, 'title':str}

    def __init__(self, title, practices, duration):
        self.title = title # название урока (строка);
        self.practices = practices # число практических занятий (целое положительное число);
        self.duration = duration #- общая длительность урока (целое положительное число).

    def __setattr__(self, __name: str, __value):
        if __name in self.attrs:
            if type(__value) != self.attrs[__name]:
                raise TypeError("Неверный тип присваиваемых данных.")
            if __name in {'practices','duration'} and __value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")   
        
        super.__setattr__(self, __name, __value)
    
    def __delattr__(self, __name: str):
        if __name in self.attrs:
            raise AttributeError()
        
    def __getattr__(self, __name: str):
        return False
        

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson:LessonItem): 
        '''- добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);'''
        self.lessons.append(lesson)

    def remove_lesson(self, indx:int):
        ''' - удаление урока по индексу в списке lessons.'''
        if indx <= len(self.lessons) - 1:
            self.lessons.pop(indx)

    def prn(self):
        for i in self.lessons:
            print(i.title)

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module:Module): 
        '''- добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);'''
        self.modules.append(module)

    def remove_module(self, indx:int):
        ''' - удаление урока по индексу в списке lessons.'''
        if indx <= len(self.modules) - 1:
            self.modules.pop(indx)

    def prn(self):
        print(self.name)
        for i in self.modules:
            print(i.name)
            i.prn()

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_2.add_lesson(LessonItem("Урок 2", -1, 1200))
# module_2.add_lesson(LessonItem(0, 1, 1200))
course.add_module(module_2)
course.prn()
module_2.lessons[0].nma2 = 'gasg'

try:
    delattr(module_2.lessons[0], 'title')
except AttributeError:
    pass
assert True, "Нt должно быть возможности удалять аттирбут"

print(module_2.lessons[0].nma2)
print(module_2.lessons[0].title )