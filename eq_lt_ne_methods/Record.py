from time import time

class Record:
    def __init__(self, *args, **kwargs):
        #for k, v in kwargs.items():
        #    self.__setattr__(k, v)
        # а можно 
        self.__dict__.update(kwargs)

    def __getitem__(self, key):
        self.__check_index__(key)
        return list(self.__dict__.values())[key]

    def __setitem__(self, key, value):
        self.__check_index__(key)
        self.__dict__[list(self.__dict__.keys())[key]] = value

    def __check_index__(self, key):
        if type(key) is int and 0 <= key < len(self.__dict__):
            return True
        raise IndexError('неверный индекс поля')

t1 = time()
r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.pk) # 1
print(r.title) # Python ООП
print(r.author) # Балакирев
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП

assert r[0] == 2 , "Не обновилось значение по индексу" 

try:
    r[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
t2 = time()
print(t2-t1)