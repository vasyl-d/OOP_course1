class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return (self.__x,self.__y)

#переменное число параметров или 2 обекта илм 4 кординаты
class Rectangle():
    def __init__(self, *args) -> None:
        if len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        else:
            self.__sp = args[0]
            self.__ep = args[1]

    def set_coords(self, sp, ep): #- изменение текущих координат, где sp, ep - объекты класса Point;
        self.__sp = sp
        self.__ep = ep

    def get_coords(self): # - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
        return (self.__sp,self.__ep)

    def draw(self): # - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")

rect = Rectangle(0, 0, 20, 34)
sp, ep = rect.get_coords()
print(sp.get_coords(), ep.get_coords())
rect.draw()