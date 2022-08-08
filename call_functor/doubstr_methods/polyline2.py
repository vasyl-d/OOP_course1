
class PolyLine:
    def __init__(self, startcoord:tuple, *args):
        self.coord_list = []
        if self.check_coords(startcoord):
            self.coord_list.append(startcoord)
        else:
            raise ValueError("startcoord must be a tuple of coordinates")
        
        if args:
            self.coord_list += [arg for arg in args if isinstance(arg, tuple) and len(arg) == 2]

    @staticmethod
    def check_coords(value):
        if isinstance(value, tuple) and len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                return True
        raise ValueError("coords must be tuple of 2 int")
    
    def add_coord(self, x, y):
        if self.check_coords((x,y)):# - добавление новой координаты (в конец);
            self.coord_list.append((x, y))

    def remove_coord(self, indx):
        # - удаление координаты по индексу (порядковому номеру, начинается с нуля);
        if indx < len(self.coord_list):
            self.coord_list.pop(indx)
    
    def get_coords(self):
        # - получение списка координат (в виде списка из кортежей).
        return self.coord_list

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
print(*poly.get_coords())
