class IteratorAttrs:
    def __iter__(self):
        for k, v in self.__dict__.items():
            yield (k, v)

    
class SmartPhone(IteratorAttrs):
    def __init__(self, model:str, size:tuple, memory:int):
        self.model, self.size, self.memory = model, size, memory

phone = SmartPhone('dfsg', (12,23), 12)
for attr, value in phone:
    print(attr, value)