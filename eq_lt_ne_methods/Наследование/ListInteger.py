class ListInteger(list):
    def TE(self):
        raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, val):
        if all(type(x) is int for x in val):
            super().__init__(val)
        else:
            self.TE()

    def __setitem__(self, key, value):
        if type(value) is int:
            super().__setitem__(key, value)
        else:
            self.TE()

    def append(self, value):
        if type(value) is int:
            super().append(value)
        else:
            self.TE()

# class ListInteger(list):
#     def __init__(self, iterable):
#         super().__init__(map(self._check_item, iterable))
    
#     def __setitem__(self, key, value):
#         super().__setitem__(key, self._check_item(value))
    
#     def _check_item(self, item):
#         if type(item) is int:
#             return item
#         raise TypeError('можно передавать только целочисленные значения')
    
#     def append(self, item):
#         super().append(self._check_item(item))

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
try:
    s[0] = 10.5 # TypeError
except TypeError:
    assert True
else:
    assert False, 'TypeError expected'