class Book:
    def __init__(self, title:str = "", author:str = "", pages:int = 0, year:int = 0):

        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, __name: str, __value) -> None:
        if (__name in {'title', 'author'} and type(__value) != str) or (__name in {'pages', 'year'} and type(__value) != int):
            raise TypeError("Неверный тип присваиваемых данных.")
        self.__dict__[__name] = __value


book = Book(title="Python ООП", author="Сергей Балакирев", pages=123, year=2022)
assert book.title == "Python ООП", 'не верное присваивание'
print(book.__dict__.values())