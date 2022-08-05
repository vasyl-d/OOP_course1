import sys

class Book:
    def __init__(self, titlte, author, pages) -> None:
        self.titlte = titlte
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга: {self.titlte}; {self.author}; {self.pages}"

lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(lst_in[0], lst_in[1], lst_in[2])

print(book)