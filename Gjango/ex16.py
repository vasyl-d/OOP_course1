'''Дана строка. Найдите первый неповторяющийся символ в этой строке и верните его индекс. 
Если такого элемента нет, то верните -1 (минус один).'''

s = input()
i = -1
for ind, el in enumerate(s):
    if s.count(el) == 1:
        i = ind
        break
print(i)

# another 

i = [ind for ind, el in enumerate(s) if s.count(el) == 1]
i = -1 if i == [] else i[0]

print(i)