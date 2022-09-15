class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration

    def __iter__(self):
        self.__value = self.start
        return self

# И создается объект этого класса командой:

g = GeomRange(1, 1.2, 2)

try:
    for x in g: print(x)
except Exception as e: print("1", str(e))

try:
    res = next(g); res = next(g)
except Exception as e: print("2", str(e))

try:
    res = next(g)
except Exception as e: print("3", str(e))
try:
    [print(x) for x in g];[print(x) for x in g]
except Exception as e: print("4",str(e))

try:
    it = iter(g); res = next(g)
except Exception as e: print("5",str(e))