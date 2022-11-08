NUM = {int, float}

class Test:
    def __init__(self, descr:str):
        if type(descr) is not str or not(10 <= len(descr) <=10000):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError

class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if (type(ans_digit) in NUM and type(max_error_digit) in NUM and max_error_digit >= 0):
            self.ans_digit = ans_digit
            self.max_error_digit = max_error_digit
        else:
            raise ValueError('недопустимые значения аргументов теста')


    def run(self):
        try:
            ans = float(input())
            return True if self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit else False
        except Exception as e:
            print(e)

if __name__ == '__main__':

    descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
    ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

    try:
        test = TestAnsDigit(descr, ans)
        print(test.run())
    except Exception as e:
        print(e)

# tests
try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"
    
try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)


try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)


