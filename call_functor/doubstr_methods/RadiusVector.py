class RadiusVector:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            if type(args[0]) is not int or args[0] <= 1:
                raise ValueError('размерность должна быть целым больше 1')
            self.size = args[0]
            self.coords = [0]*args[0]
        else:
            if self.check_coords(args):
                self.size = len(args)
                self.coords = list(args)

    def set_coords(self, *args, **kwargs):
        # - для изменения координат радиус-вектора;
        if self.check_coords(args):
            l = len(args)
            if l <= self.size:
                self.coords[0:l] = list(args)
            else:
                self.coords = list(args[0:self.size])
    def get_coords(self):
        # - для получения текущих координат радиус-вектора (в виде кортежа).
        return tuple(self.coords)
    def __len__(self):
        return self.size
    def __abs__(self):
        return sum(map(lambda x: x **2, self.coords))**(1/2)
    
    def __str__(self):
        return " ".join([str(x) for x in self.coords])

    @classmethod
    def check_coords(cls, coordinates):
        for x in coordinates:
            if type(x) not in {int, float}:
                raise TypeError("Coordinates must be integers or floats")
        return True


vector3D = RadiusVector(3)
print(vector3D)
vector3D.set_coords(3, -5.6, 8)
print(vector3D)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
print(vector3D)
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D)
res_len = len(vector3D) # res_len = 3
print(res_len)
res_abs = abs(vector3D)
print(res_abs)
