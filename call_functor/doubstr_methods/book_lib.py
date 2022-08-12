class Book:
    '''title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).'''
    def __init__(self, title:str=None, author:str=None, year:int=None):
        self.title = title
        self.author = author
        self.year = year
    

class Lib:
    def __init__(self, book_list=[]):
        if type(book_list) is not list:
            raise ValueError("Book list must be a list")
        else:
            self.book_list = book_list

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
        return self

    def __radd__(self, other):
        return self.__sum__(other)

    def __sub__ (self, other):
        if isinstance(other, Book) and other in self.book_list:
            self.book_list.remove(other)
        if isinstance(other, int) and other < len(self.book_list):
            self.book_list.pop(other)
        return self     

    def __rsub__(self, other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.book_list)

lib = Lib()
lib = lib + Book('Процесс', 'Кафка', 2020)  # добавление новой книги в библиотеку
bk1 = Book('Три товарища', 'Ремарк', 2021)
lib += bk1
lib += Book('Бесы', 'Достоевский', 2022)
lib += Book('1984', 'Оруэлл', 2022)
print(lib.__dict__)
n = len(lib) # n - число книг
print(n)
assert n == 4, "не правильно добавлется список"
lib = lib - bk1
assert len(lib) == 3, "не правильно работает удаление"
lib = lib - 0
print(lib.__dict__)
n = len(lib) # n - число книг
assert len(lib) == 2, "не правильно работает удаление"
print(lib.__dict__)
print(n)
