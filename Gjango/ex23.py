'''Валидный палиндром II
Дана непустая строка, вы можете удалить не более одного символа. 
Подумайте, сможете ли вы сделать ее палиндромом удалив всего один символ.'''
s = input()

res = False
for i in range(len(s)):
    tmp = list(s)
    tmp.pop(i)
    if tmp == tmp[::-1]:
        res = True
        break

print(res)

# print((lambda s: any([s.replace(ch, '') == s.replace(ch, '')[::-1] for ch in s]))(input()))