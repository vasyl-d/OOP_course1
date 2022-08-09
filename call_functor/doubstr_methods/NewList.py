class NewList:
    '''Class added to create a substraction to lists'''
    def __init__(self, in_list = []):
        if isinstance(in_list, list):
            self.in_list = self.li_typle(in_list)

    def get_list(self):
        return [x[0] for x in self.in_list]

    def __sub__(self, other):
        '''если значения повторяются в правом операнде - то удаляется тоже кол-во из левого и в том же порядке'''
        if isinstance(other, list):
            right = self.li_typle(other)
        elif isinstance(other, NewList):
            right = other.in_list
        else:
            raise TypeError('param is not a list or NewList')
        return NewList(self.rem_li(self.in_list, right))

    def __rsub__(self, other):
        if isinstance(other, list):
            left  = self.li_typle(other)
        elif isinstance(other, NewList):
            left = other.in_list
        else:
            raise TypeError('param is not a list or NewList')
        return NewList(self.rem_li(left, self.in_list))


    @staticmethod
    def li_typle(value:list):
        return [(x, type(x)) for x in value]

    @staticmethod
    def rem_li(left:list, right:list):
        l2 = left[:]
        for el in right:
            if el in l2:
                l2.remove(el)
        return [el[0] for el in l2]       



lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
print(lst1.get_list())
lst2 = NewList([1, 0, True])
print(lst2.get_list())

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
print(lst1.get_list())
res2 = lst1 - [0, True]
print(res2.get_list())
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], f"метод get_list вернул неверный список: {res2.get_list()}"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"