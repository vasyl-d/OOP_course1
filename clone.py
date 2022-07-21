# здесь объявляется класс Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def clone(self):
        return Point(self.x, self.y)
    
pt = Point(0,1)
pt_clone = pt.clone()

print(id(pt), id(pt_clone))
print(pt.x, pt_clone.x)
