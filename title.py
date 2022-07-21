class Book():
    def __init__(self, title = '', author = '', price = 0):
        self.__title = ''
        self.__author = ''
        self.__price = 0
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)

    def set_title(self, title): #- запись в локальное приватное свойство __title объектов класса Book значения title;
        self.__title = title
            
    def set_author(self, author): # - запись в локальное приватное свойство __author объектов класса Book значения author;
        self.__author = author
            
    def set_price(self, price): #- запись в локальное приватное свойство __price объектов класса Book значения price;
        if type(price) is int and price >= 0:
            self.__price = price
        else:
            raise "не правильная цена"
        
    def get_title(self): # - получение значения локального приватного свойства __title объектов класса Book;
        return self.__title
    
    def get_author(self): # - получение значения локального приватного свойства __author объектов класса Book;
        return self.__author
    
    def get_price(self): # - получение значения локального приватного свойства __price объектов класса Book;
        return self.__price


book = Book('ddd','asdg', 100)
b1 = Book('second','author',200)
print(book.get_author())