'''Наибольний общий префикс для строк'''
s = input().split(',')
i, val = min(map(lambda x: (len(x),x), s))
s.remove(val)
res = ''
for i in range(1, i):
    cur = val[:i]
    if any(map(lambda x: cur != x[:i], s)):
        break
    else:
        res = cur

print(res)
