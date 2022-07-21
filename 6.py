# здесь объявите класс TriangleChecker
NORM_TYPE = (int, float)

class TriangleChecker:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        
    def is_triangle(self):
        for it in self.__dict__:
            if type(self.__dict__.get(it)) not in NORM_TYPE:
                print(self.__dict__.get(it), type(self.__dict__.get(it)))
                return 1
            elif self.__dict__.get(it) <= 0:
                return 1
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            return 2
        return 3 

a, b, c = map(int, input().split()) # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())