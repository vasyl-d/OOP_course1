from re import findall
class Morph:
    def __init__(self, *args):
        self.forms = args if args else []

    def add_word(self, word:str): 
        #- добавление нового слова (если его нет в списке слов объекта класса Morph);
        if type(word) is str:
            self.forms.append(word)

    def get_words(self):
        # - получение кортежа форм слов.
        return tuple(self.forms)

    def __eq__(self, __o: object) -> bool:
        if type(__o) is str:
            if __o.lower() in self.forms:
                return True
        return False

    def __ne__(self, __o: object) -> bool:
        return False if __o.lower() in self.forms else True


s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]
print([el.get_words() for el in dict_words])
#text = input()
text = "Мы будем устанавливать связь завтра днем."
#print(len([el for el in dict_words if el in findall("(\w+)",text.lower())]))
print(len([el for el in findall("(\w+)",text.lower()) if el in dict_words]))


assert "связи" == dict_words[0], "не работает =="
assert dict_words[0] == "связи", "не работает =="
