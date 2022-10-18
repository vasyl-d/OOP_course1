from abc import ABC, abstractmethod

class CountryInterface(ABC):
    @abstractmethod
    def get_info(self):
        """Метод для перемещения транспортного средства"""
        pass

    @property
    @abstractmethod
    def name(self):
        """Абстрактный объект-свойство"""
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

def TE():
    raise TypeError("My be a correct type")

class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.name, self.population, self.square = name, population, square
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name if type(name) is str else TE()      

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population if type(population) is int and population > 0 else TE()

    @property
    def square(self):
        return self.__square
    
    @square.setter
    def square(self, square):
        self.__square = square if type(square) in {int, float} and square > 0 else TE()

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"

# 
country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000