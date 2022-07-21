class RadiusVector2D:
    MIN_COORD = -100 
    MAX_COORD = 1024
    def __init__(self, x=0,y=0) -> None:
        self.__x = x if self.is_norm(x) else 0
        self.__y = y if self.is_norm(y) else 0
            

    def is_norm(self, x):
        return True if type(x) in (int, float) and self.MIN_COORD <= x <=self.MAX_COORD else False

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if self.is_norm(x):
            self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if self.is_norm(y):
            self.__y = y    

    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2

v1 = RadiusVector2D(-200, 2000)
print(v1.x, v1.y)
v1 = RadiusVector2D(-200, 'a')
v1.y = 'b'
print(v1.x, v1.y)
v2 = RadiusVector2D(2,3)
print(RadiusVector2D.norm2(v2))