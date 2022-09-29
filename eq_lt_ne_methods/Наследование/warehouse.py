class Thing:
    def __init__(self, name:str, weight:float):
        self.name, self.weight = name, weight

class ArtObject(Thing):
    def __init__(self, name:str, weight:float, author:str, date:str):
        super().__init__(name, weight)
        self.author, self.date = author, date

class Computer(Thing):
    def __init__(self, name:str, weight:float, memory:int, cpu:str):
        super().__init__(name, weight)
        self.memory, self.cpu = memory, cpu

class Auto(Thing):
    def __init__(self, name:str, weight:float, dims:tuple):
        super().__init__(name, weight)
        self.dims = dims

class Mercedes(Auto):
    def __init__(self, name:str, weight:float, dims:tuple, model:str, old:int):
        super().__init__(name, weight, dims)
        self.model, self.old = model, old

class Toyota(Auto):
    def __init__(self, name:str, weight:float, dims:tuple, model:str, wheel:bool=False):
        super().__init__(name, weight, dims)
        self.model, self.wheel = model, wheel       
