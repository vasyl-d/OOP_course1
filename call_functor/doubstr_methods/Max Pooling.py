from numpy import array
NUM = {int, float}

class MaxPooling:
    def __init__(self, step:tuple=(2,2), size:tuple=(2,2)):
        self.step=step
        self.size=size
        
    def __call__(self, matrix:list):
        max_list = []
        if self.check_value(matrix):
            arr = array(matrix)
            mx = arr.shape
            row_lim = (mx[0] - self.size[0])//self.step[0]+self.step[0]
            col_lim = (mx[1] - self.size[1])//self.step[1]+self.step[1]
            for i in range(0, row_lim, self.step[0]):
                r_list = []
                for j in range(0, col_lim, self.step[1]):
                    r_list.append(arr[i:self.size[0]+i,j:self.size[1]+j].max())
                max_list.append(r_list)
        return max_list
        
    @classmethod
    def check_value(cls, value):
        if type(value) != list:
            raise ValueError("Неверный формат для первого параметра matrix.")
        
        l = len(value)
        for i in value:
            if len(i) != l:
                raise ValueError("Неверный формат для первого параметра matrix.")

            for j in i:
                if type(j) not in NUM:
                    raise ValueError("Неверный формат для первого параметра matrix.")
        return True

#tests
mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
res1 = mp(m1)
assert res1 == [[10]], f"неверный результат операции MaxPooling {res1}"

m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res2 = mp(m2)
assert res2 == [[10, 12], [40, 300]], f"неверный результат операции MaxPooling {res2}"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"