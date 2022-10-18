def TE():
    raise TypeError('значение не соответствует типу объекта')

class Digit:
    def __init__(self, value):
        super().__init__()
        self.value = value if type(value) in {int, float} else TE()

    def __str__(self):
        return str(self.value)

class Integer(Digit):
    #  value - целое число;
    def __init__(self, value):
        super().__init__(value)
        self.value = value if type(value) is int else TE()

class Float(Digit):
    #  value - вещественное число;
    def __init__(self, value):
        super().__init__(value)
        self.value = value if type(value) is float else TE()   

class Positive(Digit):
    #  value - положительное число;
    def __init__(self, value):
        super().__init__(value)
        self.value = value if value >= 0 else TE()

class Negative(Digit): 
    # value - отрицательное число.
    def __init__(self, value):
        super().__init__(value)
        self.value = value if value < 0 else TE()

class PrimeNumber(Integer, Positive):
    # простые числа; наследуется от классов Integer и Positive;
    pass

class FloatPositive(Float, Positive):
    #  - наследуется от классов Float и Positive.
    pass


digits = [
        PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
        FloatPositive(3.5), FloatPositive(8.9)
        ]

# Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

# lst_positive - все объекты, относящиеся к классу Positive;
lst_positive = filter(lambda x: isinstance(x, Positive), digits)

# lst_float - все объекты, относящиеся к классу Float. 
lst_float = filter(lambda x: isinstance(x, Float), digits) 

print(*lst_positive)
print(*lst_float)