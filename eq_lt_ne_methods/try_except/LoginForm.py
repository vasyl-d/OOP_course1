class ValidatorString:
    __slots__ = 'min_length', 'max_length', 'chars'
    def __init__(self, min_length:int, max_length:int, chars:str='') -> None:
        self.min_length, self.max_length, self.chars = min_length, max_length, chars

    def is_valid(self, string:str)->bool:
        if type(string) is str and self.min_length <= len(string) <= self.max_length:
            if self.chars > '':
                if set(string).intersection(set(self.chars)):
                    return string
            else:
                return string
        raise ValueError('недопустимая строка')

    def __call__(self, string:str):
        return self.is_valid(string)

class LoginForm:
    __slots__ = 'login_validator', 'password_validator','_login', '_password'
    def __init__(self, login_validator:ValidatorString, password_validator:ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request:dict):
        try:
            self._login = self.login_validator(request['login'])
            self._password = self.password_validator(request['password'])
        except KeyError:
            raise TypeError('в запросе отсутствует логин или пароль')

# 
login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)