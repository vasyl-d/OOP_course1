class Body:
    def __init__(self, name, ro=0, volume=0):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_m(self):
        return self.ro*self.volume

    @staticmethod
    def check_value(__o):
        if type(__o) is Body:
            return __o.get_m()
        elif type(__o) in {int, float}:
            return __o
        else:
            raise TypeError("object Body or int or float expected")

    def __eq__(self, __o: object) -> bool:
        return True if self.get_m() == self.check_value(__o) else False

    def __lt__(self, __o: object) -> bool:
        return True if self.get_m() < self.check_value(__o) else False
    
    def __gt__(self, __o: object) -> bool:
        return True if self.get_m() > self.check_value(__o) else False


'''Есть красивый вариант с декоратором
def mass_arg(func):
	def wrapper(instance, other, *args):
		if isinstance(other, Body): 
			return func(instance, other.mass)
		elif isinstance(other, (int, float)):
			return func(instance, other)
		else:
			raise TypeError(f"Not supported type {type(other)} in {func}")
	return wrapper

тогда 

	@mass_arg	
	def __lt__(self, other):
		return (self.mass < other)
		
	@mass_arg
	def __le__(self, other):
		return self.mass <= other
	
	@mass_arg
	def __eq__(self, other):
		return self.mass == other
'''

body1 = Body('Стол', 1, 10)
body2 = Body('Стул', 1, 5)

assert body1 > body2, "не работает сравнение с объектом "  # True, если масса тела body1 больше массы тела body2
assert body1 != body2, "не работает равенство c собъектом" # True, если масса тела body1 не равна массе тела body2
assert body1 < 11, "Не раотает меньше с числом"     # True, если масса тела body1 меньше 10
assert body2 == 5, 'не работает равенство с чслом'    # True, если масса тела body2 равна 5
assert body1 > 5, "Не раотает больше с числом"     # True, если масса тела body1 больше 5
