import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        for i in data:
            self.lst_data += [{self.FIELDS[ind]:val for ind, val in enumerate(i.split())}]
            #или так: self.lst_data += [dict(zip(self.FIELDS, i.split()))]
            
    def select(self, a, b):
        b1 = len(self.lst_data)
        if b > b1:
            b = b1
        if a > b1 or a > b:
            return []
        return self.lst_data[a:b+1]
            
db = DataBase()
db.insert(lst_in)
print(*db.select(1, 2))