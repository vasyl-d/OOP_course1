class Animal:
    def __init__(self, name:str, kind:str, old:int):
        self.name, self.kind, self.old = name, kind, old

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) is str:
            self.__name = value
        else:
            raise ValueError("Value must be a string")

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if type(value) is str:
            self.__kind = value
        else:
            raise ValueError("Value must be a string")

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        if type(value) is int:
            self.__old = value
        else:
            raise ValueError("Value must be an int")

animals = [Animal("Васька", "дворовый кот", 5), Animal("Рекс","немецкая овчарка", 8), Animal("Кеша", "попугай", 3)]