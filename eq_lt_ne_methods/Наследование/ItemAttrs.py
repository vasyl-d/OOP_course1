# класс для доступа к атрибутам по индексу
# но можно было и от List его унаследовать  
class ItemAttrs:
    def __getitem__(self, key):
        return list(self.__dict__.values())[key]

    def __setitem__(self, key, value):
        self.__setattr__(list(self.__dict__.keys())[key], value)

class Point(ItemAttrs):
    def __init__(self, x:int, y:int):
        super().__init__()
        self.x, self.y = x, y

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
print(pt.x, pt.y)