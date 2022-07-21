import sys

class StreamData:
    def create(self, fields, lst_values):
        '''Если создание локальных свойств проходит успешно, то метод create() 
        возвращает True, иначе - False. Если число полей и число строк не совпадает,
         то метод create() возвращает False.'''
        if len(fields) != len(lst_values):
            return False
        for i, v in enumerate(fields):
            setattr(self, v, lst_values[i])
            if not getattr(self, v):
                return False
        return True
        


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data)
print(result)