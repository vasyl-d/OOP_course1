def func_decorator(func, log_list):
    def wrapper(self, *args, **kwargs):
        log_list.append(func.__name__)
        return func(self, *args, **kwargs)
    return wrapper

def class_log(vector_log):
#функция парметризатор
    def class_log(cls, *args, **kwargs) :
    # функция модифицирует методы класса, добавляя к ним вызов функции 
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, func_decorator(v, vector_log))

        return cls
    return class_log

vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

# 

v = Vector(1, 2, 3)
v[0] = 10
print(*vector_log)