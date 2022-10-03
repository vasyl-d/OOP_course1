def str_params_decorated(func):
    def wrapper(self, *args, **kwargs):
        if any(not x.isdigit() for x in args) or any(not x.isdigit() for x in kwargs.values()):
            raise ValueError("в строке должны быть только цифры")
        return func(self, *args, **kwargs)
    return wrapper


def str_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, str_params_decorated(v))
    return cls

@str_params
class StringDigit(str):
    def __init__(self, string):
        super().__init__()

    def __add__(self, other):
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit(other.__add__(self))

sd = StringDigit("123")
print(sd)       # 123
print(type(sd))
sd = sd + "456" # StringDigit: 123456
print(sd)       
print(type(sd))
sd = "789" + sd # StringDigit: 789123456
assert sd == "789123456" and type(sd) is StringDigit, "Invalid radd"


try:
    sd = sd + "12f" # ValueError
except ValueError:
    assert True 
else:
    assert False, "must be value error"