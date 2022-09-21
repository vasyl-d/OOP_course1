class Animal:
    def __init__(self, name, old) -> None:
        self.name = name
        self.old = old

    def get_info(self):
        d_s = ', '.join((str(self.__dict__[k]) for k, v in self.__dict__.items() if k not in {'name','old'})) 
        return f"{self.name}: {self.old}, {d_s}"

class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

class Dog(Animal):
    def __init__(self, name, old, breed:str, size:tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

cat = Cat('кот', 4, 'black', 2.25)
dog = Dog('пёс', 4, 'хаски', (2, 3))
print(cat.get_info())
print(dog.get_info())