class Validator:
    def _is_valid(self, value):
        return True

    def __call__(self, value):
        if not self._is_valid(value):
            raise ValueError('данные не прошли валидацию')

class NumValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value, self.max_value = min_value, max_value

class IntegerValidator(NumValidator):
    def _is_valid(self, value):
        return True if type(value) is int and self.min_value <= value <= self.max_value else False

class FloatValidator(NumValidator):
    def _is_valid(self, value):
        return True if type(value) is float and self.min_value <= value <= self.max_value else False

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)

try:
    res2 = integer_validator('3')    # исключение ValueError
except ValueError:
    assert True
else:
    assert False, "Не сгенерировалось исключение"


try:
    res2 = float_validator(10.0)    # исключение ValueError
except ValueError:
    assert True
else:
    assert False, "Не сгенерировалось исключение"

try:
    res2 = float_validator(0.01)    # норм
except ValueError:
    assert False, "неправильное исключение"
else:
    assert True