from random import randint, choices

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        '''psw_chars - строка из разрешенных в пароле символов; min_length, max_length - минимальная и максимальная длина генерируемых паролей.'''
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwds):
        k = randint(self.__min_length, self.__max_length)
        return ''.join(choices(self.__psw_chars, k = k))


min_length, max_length = 5, 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)

p1 = rnd()
p2 = rnd()

lst_pass = [rnd() for _ in range(3)]

print(p1, p2)
print(*lst_pass)