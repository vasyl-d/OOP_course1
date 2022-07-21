from time import time
import re

class EmailValidator():
    def __new__(cls) -> None:
        return None

    '''- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
    - длина email до символа @ не должна превышать 100 (сто включительно);
    - длина email после символа @ не должна быть больше 50 (включительно);
    - после символа @ обязательно должна идти хотя бы одна точка;
    - не должно быть двух точек подряд.'''
    @classmethod
    def check_email(cls, email): # - возвращает True, если email записан верно и False - в противном случае;
        if not cls.__is_email_str(email):
            return False
        if '..' in email or '@' not in email:
            return False
        s = email.split('@')
        if '.' not in s[1]:
            return False
        if re.fullmatch('(?:[.\w]{1,100})@(?:[.\w]{1,50})', email) == None:
            return False
        return True

    @classmethod    
    def get_random_email(cls): # - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).
        return str(time())+'@gmail.com'

    def __is_email_str(email):
        if type(email) != str:
            return False
        return True

assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False