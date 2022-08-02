from string import ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    '''lv = LengthValidator(min_length, max_length) 
    min_length - минимально допустимая длина; max_length - максимально допустимая длина'''
    def __init__(self, min_length=None, max_length=None):
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwds):
        return True if self.__min_length <= len(args[0]) <= self.__max_length else False

class CharsValidator:
    '''cv = CharsValidator(chars) # chars - строка из допустимых символов'''
    def __init__(self, chars=None):
        self.__chars = chars
    
    def __call__(self, *args, **kwds):
        return set(self.__chars).issuperset(set(args[0]))


from string import ascii_lowercase, digits

lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
else:
    print('Error')

cv = CharsValidator(ascii_lowercase + digits)

print(cv('panda'))