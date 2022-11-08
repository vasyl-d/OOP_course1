class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        super().__init__()
        if kwargs:
            k,v = list(kwargs.items())[0]
            self.msg = f"Значение первичного ключа {k} = {v} недопустимо"
        else:
            self.msg = "Первичный ключ должен быть целым неотрицательным числом"
        
    def __str__(self) -> str:
        return self.msg

# 

e1 = PrimaryKeyError(id = -10.5,)
try:
    raise e1
except PrimaryKeyError as e:
    print(e)

# 

e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо

print(e1, e2, e3)

#test
assert issubclass(PrimaryKeyError, Exception), "класс PrimaryKeyError должен наследоваться от класса Exception"

e1 = PrimaryKeyError(id=1)
e2 = PrimaryKeyError(pk=2)
e3 = PrimaryKeyError()

assert str(e1) == "Значение первичного ключа id = 1 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
assert str(e2) == "Значение первичного ключа pk = 2 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
assert str(e3) == "Первичный ключ должен быть целым неотрицательным числом", "неверное сообщение для исключения объекта класса PrimaryKeyError"