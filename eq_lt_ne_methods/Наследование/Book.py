FRM = {'pdf', 'doc', 'fb2', 'txt'}

class Book:
    def __init__(self, title:str, author:str, pages:int, year:int):
        self.title, self.author, self.pages, self.year = title, author, pages, year

class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size, self.frm = size, frm