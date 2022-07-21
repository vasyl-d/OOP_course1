class LineTo:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args) -> None:
        self.path = []
        if args is not None:
            for l in args:
                if type(l) is LineTo:
                    self.path += [l]

    def get_path(self):
         #- возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
         return self.path

    def get_length(self): 
        # - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
        path_len = 0.0
        l = len(self.path)
        if l >= 1:
            path_len += ((self.path[0].x-0)**2 + (self.path[0].y-0)**2)**(1/2)
        for i in range(1, l):
            path_len += ((self.path[i].x-self.path[i-1].x)**2 + (self.path[i].y-self.path[i-1].y)**2)**(1/2)
        return path_len

        
    def add_line(self, line):
        # - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
        if type(line) is LineTo: 
            self.path += [line]



p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []