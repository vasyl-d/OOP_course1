class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    
    def __bool__(self):
        return hasattr(self, "x1") and hasattr(self, "y1") and hasattr(self, "x2") and hasattr(self, "y2")

    def get_coords(self):
        # для получения кортежа текущих координат объекта.
        if self:
            return (self.x1, self.y1, self.x2, self.y2)
        raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 4, 4), Ellipse(0, 0, 3, 3)]

lst_out = [el.get_coords() for el in lst_geom if el]

print(*lst_out)