class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        print('validation')

        self.__name = value.upper()


p = Person("Ivan")
assert p.name == "Ivan"

class Car:
    def __init__(self, model=None):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if self.__check_model(value):
            self.__model = value

    @staticmethod
    def __check_model(value):
        return True if type(value) == str and 2 <= len(value) <= 100 else False 

assert Car("Toy").model == "Toy"
c = Car()
c.model = "waz"
assert c.model == "waz"


class WindowDlg:
    '''заголовок окна, ширина, высота
    В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:

    __title - заголовок окна (строка);
    __height, __width - ширина и высота окна (числа).'''
    def __init__(self, title='', width=0, height=0) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title        

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if self.is_par(width):
            self.__width = width
            self.show()   

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if self.is_par(height):
            self.__height = height 
            self.show() 

    @staticmethod
    def is_par(par):
        return True if type(par) == int and 0 <= par <= 10000 else False

    def show(self): 
         '''для отображения окна на экране (выводит в консоль строку в формате: 
         "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").'''
         print(f"{self.__title}: {self.__width}, {self.__height}")  


wi = WindowDlg('title', 100, 50)
wi.height = 200
wi.width = 100 