
NUM = {int, float}
class Dimensions:
    def __init__(self, a, b, c):
        #a, b, c - положительные числа (целые или вещественные)
        self.a = self.check(a)
        self.b = self.check(b)
        self.c = self.check(c)

    @staticmethod
    def check(value):
        if type(value) in NUM and value >=0:
            return value
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")


    def __hash__(self) -> int:
        return hash((self.a * self.b * self.c))

    def __gt__(self, other):
        return hash(self) > hash(other)

s_inp = "1 2 3; 4 5 6.78; -1 2 3; 0 1 2.5"
lst_dims = [Dimensions(*tuple(map(float, i.strip().split(' ')))) for i in s_inp.split(';')]
print(lst_dims)
lst_dims = sorted(lst_dims)
[print(i.a, i.b, i.c) for i in lst_dims]