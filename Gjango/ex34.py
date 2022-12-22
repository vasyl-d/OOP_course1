'''Ваш друг набирает свое имя на клавиатуре. Иногда при вводе символа клавиша может залипнуть, и символ будет набран 1 или более раз.

Вы изучаете набранные на клавиатуре символы. Верните True, если возможно, что это было имя вашего друга, причем некоторые символы 
(возможно, ни один) были так же набраны несколько раз.'''
name = input()
typed = input()

def make_dict(string:str)->dict:
    cnt = 1
    res = dict()
    for ind in range(1, len(string)):
        if string[ind] == string [ind - 1]:
            cnt += 1
        else:
            res[string[ind-1]] = cnt
            cnt = 1
    res[string[-1]] = cnt
    return res

def check_name(name: str, typed:str)-> bool:
    d1 = make_dict(name)
    d2 = make_dict(typed)

    return d1.keys() == d2.keys() and all(map(lambda x: x[1] >= x[0], zip(d1.values(), d2.values())))

print(check_name(name, typed))


assert check_name("alex", "aaleex") == True
assert check_name("saeed", "ssaaedd") == False