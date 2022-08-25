import sys

class BookStudy:
    #name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число).
    def __init__(self,name:str = "", author:str = "", year:int = 0):
        self.name = name
        self.author = author
        self.year = year
    
    def __hash__(self) -> int:
        #вычисление хэша по двум атрибутам: name и author (без учета регистра)
        return hash((self.name.lower(), self.author.lower()))


#lst_in = list(map(str.strip, sys.stdin.readlines())) 

s= '''Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021'''

lst_in = [line for line in s.splitlines()]
lst_bs = []
for l in lst_in:
    ss = l.split(';')
    lst_bs.append(BookStudy(ss[0], ss[1], int(ss[2])))

h = set(map(hash, lst_bs))
unique_books = len(h)