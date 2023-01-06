'''Наибольший общий делитель строк
Для двух строк s и t мы говорим "t делит s" тогда и только тогда, когда s = t + ... + t (t сцеплено с самим собой 1 или более раз)

Дано две строки str1 и str2, верните самую большую строку x, такую что x делит как str1, так и str2.'''

def str2str(str1, str2):
    return str1*(int(len(str2)/len(str1))) == str2 

# str1 = input()

# str2 = input()

def nod2str(str1, str2):
    if not (str2 in str1 or str1 in str2):
        return('')

    start = str1 if len(str1) < len(str2) else str2

    for i in range(len(start), 1, -1):
        nod = start[:i:]
        if str2str(nod, str1) and str2str(nod, str2):
            return(nod)
    return('')

test = [("ABCABC","ABC", "ABC"),
        ('ABABAB','ABAB',"AB"),
        ('STE', 'PIK', '')
        ]

for x in test:
    print(nod2str(x[0],x[1]), x[2])