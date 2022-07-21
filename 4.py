class Translator:
    en_ru_dict = {}
    def add(self, eng, rus):
        r1 = self.translate(eng)
        if r1 != []:
            self.en_ru_dict.update({eng: r1+[rus]})
        else:    
            self.en_ru_dict[eng] = [rus]
        
    def remove(self, eng):
        return self.en_ru_dict.pop(eng)
        
    def translate(self, eng):
        return self.en_ru_dict.get(eng, [])
        
        
tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))