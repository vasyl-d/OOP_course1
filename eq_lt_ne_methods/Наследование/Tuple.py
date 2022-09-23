from time import time

class Tuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            # return Tuple(list(self) + (list(el for el in other)))    
            return __class__((*self,*other))      #так чуток быстрее
        else:
            raise TypeError("must be iterable")
    
    def __radd__(self, other):
        return self.__add__(other)

t1 = time()

a = [1,2,3]
b = (1,2,3)
c = Tuple(b)
print(c)
d = c+b
print(d)

t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)
t2= time()
print(t2-t1)