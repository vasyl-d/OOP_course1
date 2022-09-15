class Person:    
    def __init__(self, fio:str, job:str, old:int, salary, year_job:int):
        self.fio, self.job, self.old, self.salary, self.year_job = fio, job, old, salary, year_job

    def __getitem__(self, key):
        return list(self.__dict__.values())[self.check(key)]

    def __setitem__(self, key, value):
        attr = list(self.__dict__.keys())[self.check(key)]
        self.__setattr__(attr, value)

    @staticmethod
    def SI():
        raise StopIteration

      
    @staticmethod
    def check(value):
        if type(value) is int and 0 <= value <= 4:
            return value
        raise IndexError('неверный индекс')

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError