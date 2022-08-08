class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if self.check_value(value):
            self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if self.check_value(value):
            self.__img = value

    @classmethod
    def check_value(cls, value):
        if type(value) in {int, float}:
            return True
        raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return (self.real**2 + self.img**2)**(1/2)

    def __str__(self):
        return "Complex(%s,%s)" % (self.real, self.img)


cmp = Complex(7,8)
#print(cmp)
cmp.real = 3
cmp.img = 4
#print(cmp)

c_abs= abs(cmp)
#print(c_abs)