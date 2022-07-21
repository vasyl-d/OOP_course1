# Здесь объявляется класс Factory
class Factory():
    @staticmethod
    def build_sequence(): # для создания начального пустого списка (метод должен возвращать пустой список);
        return []
    
    @staticmethod
    def build_number(string): # для преобразования переданной в метод строки (string) в вещественное значение (метод должен возвращать полученное вещественное число).
        return float(string)




class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
#s = input()
s = "4, 5, -6.5"
res = ld.parse_format(s, Factory())
print(res)