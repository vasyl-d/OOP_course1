'''Найти индексы элементов массива, котороые дают в сумме искомое число'''
x = input().split(',')

y = int(input())

res = []
x = list(map(int,x))
for i, v in enumerate(x):
    for j, e in enumerate(x[i+1:]):
        if v + e == y:
            res = [i,j+i+1]
            break
    if res != []:
        break

print(res)

# print([[i, j] for i in range(len(x)) for j in range(i+1, len(x)) if x[i]+x[j] == y][0])