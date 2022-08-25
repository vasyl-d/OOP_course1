class Player:
    '''name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число)'''
    def __init__(self, name, old:int, score:int):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return self.score > 0
    
    def __str__(self) -> str:
        return f"name: {self.name}, score: {self.score}, old: {self.old}"

    
s = '''Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0'''

lst_in = list(map(str.strip, s.splitlines()))
players = [Player(*el.split(';')) for el in lst_in]
[print(el) for el in players]
players_filtered = list(filter(bool, players))
print('filtered:')
[print(el) for el in players_filtered]