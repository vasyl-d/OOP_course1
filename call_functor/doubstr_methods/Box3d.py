NUM = {int, float}

class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width + other.width, self.height+other.height, self.depth+other.depth)
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)
    def __rsub__(self, other):
        if isinstance(other, Box3D):
            return other.__sub__(self)
    def __mul__(self, other):
        if type(other) in NUM:
            return Box3D(self.width * other, self.height * other, self.depth * other)
    def __rmul__(self, other):
        return self.__mul__(other)
    
    '''для целочисленного деления - __floordiv__, для вычисления остатка от деления - __mod__'''
    def __floordiv__(self, other):
       if type(other) in NUM:
            return Box3D(self.width // other, self.height // other, self.depth // other)
    def __mod__(self, other):
       if type(other) in NUM:
            return Box3D(self.width % other, self.height % other, self.depth % other)

    def __str__(self):
        return f"x: %d, y: %d, z: %d" % (self.width, self.height, self.depth)

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
print(box)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
print(box)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
print(box)
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
print(box)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
print(box)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
print(box)