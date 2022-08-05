class WordString:
    def __init__(self, string=""):
        self.__string = string

    @property    
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string

    def __str__(self):
        return self.__string
    
    def __len__(self):
        s = self.str_strip(self.__string)
        s = s.split(' ')
        return len(s)

    def __call__(self, indx):
        s = self.str_strip(self.__string)
        s = s.split(' ')
        return s[indx] if 0 <= indx <= len(s) else None

    @classmethod
    def str_strip(self, string):
        s = string
        while s.find("  ") > 0:
            s = s.replace("  ", " ")
        return s

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")

words = WordString("Курс по Python    ООП от  Сергея Балакирева")
assert words.string == "Курс по Python    ООП от  Сергея Балакирева", "объект-свойство string вернуло невереные данные"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")