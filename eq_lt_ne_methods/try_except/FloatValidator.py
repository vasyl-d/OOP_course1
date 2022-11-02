class NumValidator:
    __slots__ = 'min_value', 'max_value'
    def __init__(self, min_value, max_value):
        self.min_value, self.max_value = min_value, max_value

def VE():
    raise ValueError('значение не прошло валидацию')

class FloatValidator(NumValidator):
    def __call__(self, value):
        return True if self.min_value <= value <= self.max_value and type(value) == float else VE()

class IntegerValidator(NumValidator):
    def __call__(self, value):
        return True if self.min_value <= value <= self.max_value and type(value) == int else VE()
        

def is_valid(lst:list, validators:list):
    res = []
    for el in lst:
        for val in validators:
            try:
                if val(el):
                    res.append(el)
                    break
            except:
                pass
    return res

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)