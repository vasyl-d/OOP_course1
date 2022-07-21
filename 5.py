'''Создаем 217 обектов случайно одного из 3х классов со случайными координатами'''
from random import choice, randint

class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Line(Figure):
    pass

class Rect(Figure):
    pass

class Ellipse(Figure):
    pass

func = [Line, Rect, Ellipse]

elements = [choice(func)(randint(0, 200),randint(0, 200),randint(0, 200),randint(0, 200)) for i in range(217)]

for i in elements:
    if type(i) is Line:
        i.sp = (0,0)
        i.ep = (0,0)

[print(i.sp, i.ep, type(i)) for i in elements]