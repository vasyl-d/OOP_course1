class Validator:
    def _is_valid(self, value):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

    def __call__(self, value):
        return True if self._is_valid(value) else False
            

class NumValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value, self.max_value = min_value, max_value

class IntegerValidator(NumValidator):
    def _is_valid(self, value):
        return True if type(value) is int and self.min_value <= value <= self.max_value else False

class FloatValidator(NumValidator):
    def _is_valid(self, value):
        return True if type(value) is float and self.min_value <= value <= self.max_value else False

iv = IntegerValidator(-10, 10)
fv = FloatValidator(-1, 10)
print(iv(10))  # исключение не генерируется (проверка проходит)
print(fv(5.5))
print(fv(1))