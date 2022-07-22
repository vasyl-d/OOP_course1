class ValidateString:

    def __init__(self, min_lenght=3, max_lenght=100) -> None:
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght

    def validate(self, string):
        return True if type(string) == str and self.min_lenght <=len(string) <= self.max_lenght else False


class StringValue:
    #descriptor
    def __init__(self, validator:ValidateString=ValidateString()) -> None:
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validator=ValidateString()) # для ввода логина;
    password = StringValue(validator=ValidateString())  # для ввода пароля;
    email = StringValue(validator=ValidateString())  # для ввода Email.

    def __init__(self, login, password, email) -> None:
        self.email = email
        self.login = login
        self.password = password

    def get_fields(self): #- возвращает список из значений полей в порядке [login, password, email];
        return [self.login, self.password, self.email]

    def show(self): # выводит в консоль многострочную строку в формате:
        print(f"<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>")
        

#проверки
assert hasattr(ValidateString, 'validate'), "в классе ValidateString отсутствует метод validate"

r = RegisterForm('11111', '1111111', '11111111')
assert hasattr(r,'login') and hasattr(r, 'password') and hasattr(r, 'email'), "в классе RegisterForm должны быть дескрипторы login, password, email"

assert hasattr(RegisterForm, 'show'), "в классе RegisterForm отсутствует метод show"

r.show()


StringValue.__doc__

frm = RegisterForm("123", "2345", "sc_lib@list.ru")
assert frm.get_fields() == ["123", "2345", "sc_lib@list.ru"], "метод get_fields вернул неверные данные"

frm.login = "root"
assert frm.login == "root", "дескриптор login вернул неверные данные"

v = ValidateString(5, 10)
assert v.validate("hello"), "метод validate вернул неверное значение"
assert v.validate("hell") == False, "метод validate вернул неверное значение"
assert v.validate("hello world!") == False, "метод validate вернул неверное значение"


class A:
    st = StringValue(validator=ValidateString(3, 10))


a = A()
a.st = "hello"

assert a.st == "hello", "дескриптор StringValue вернул неверное значение"
a.st = "d"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной меньше min_length"
a.st = "dапарпаропропропропр"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной больше max_length"
a.st = "dапарпароп"
assert a.st == "dапарпароп", "дескриптор StringValue сохранил строку длиной больше max_length"