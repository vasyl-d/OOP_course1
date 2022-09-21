class Singleton:
    __instance_id = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance_id is None:
            cls.__instance_id = super().__new__(cls)
        return cls.__instance_id
    
    def __del__(self):
        Singleton.__instance_id = None

        
class Game(Singleton):
    name = None
    def __init__(self, name):
        if self.name is None:
            self.name = name  

g = Game('ddd')
print(g.__dict__)
b = Game('bbb')
print(b.name)
print(g.__dict__)
print(b.__dict__)