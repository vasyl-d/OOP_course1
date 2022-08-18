'''Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова 
и разбить строку по словам (слова разделяются одним или несколькими пробелами). 
На основе полученного списка слов, создать объект класса StringText'''
from re import findall

TRIM_CHR = "–?!,.;"

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__(self, lst_words:list=[]):
        self.lst_words = lst_words
        
    def __len__(self):
        return len(self.lst_words)

    def __str__(self) -> str:
        return ' '.join(self.lst_words)

    def __eq__(self, __o: object) -> bool:
        l = len(self)
        if type(__o) is int:
            if l == __o:
                return True
        if type(__o) is StringText:
            if l == len(__o):
                return True
        return False
    def __lt__(self, __o: object) -> bool:
        l = len(self)
        if type(__o) is int:
            if l < __o:
                return True
        if type(__o) is StringText:
            if l < len(__o):
                return True
        return False

    def __le__(self, __o: object) -> bool:
        l = len(self)
        if type(__o) is int:
            if l <= __o:
                return True
        if type(__o) is StringText:
            if l <= len(__o):
                return True
        return False

lst_text = [StringText(findall("(\w+)", str)) for str in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [str(el) for el in lst_text_sorted]
#print(lst_text_sorted)