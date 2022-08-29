class Value:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if type(value) not in {int, float}:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)  

class Line:
    x1: Value()
    x2: Value()
    y1: Value()
    y2: Value()
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return int(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**(1/2))
        

l1 = Line(0, 0, 2, 2)
print(len(l1))
l2 = Line(0, 0, 0.1, 0.5)
print(len(l2))