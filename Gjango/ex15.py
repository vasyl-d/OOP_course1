'''Предположим вы пишите требование о выкупе ransomNote из вырезанных букв из журнала magazine. Верни True, если из вырезанных 
букв из журнала можно составить записку о выкупе. Учти, каждую букву из журнала можно использовать только 1 раз.'''
ransomNote = input()
magazine = list(input())

try:
    for el in ransomNote:
        magazine.remove(el) 
except ValueError:
    print(False)
else:
    print(True)

# или просто ransomNote in magazine