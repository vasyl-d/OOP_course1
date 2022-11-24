'''Дана строка, проверьте, может ли она состоять из повторяющихся подстрок.
на самом деле достаточно проверить последовательности длиной 2х символов'''
s = input()

l = int(len(s)/2)
res = False
for window in range(2, l+1):
    for ind in range(0, l):
        ss = s[ind: ind+window]
        print(ss)
        if s.count(ss) > 1:
            res = True
            break
    if res:
        break

print(res)

# 
res = False
window = 2
for ind in range(0, len(s)-1):
    ss = s[ind: ind+window]
    print(ss)
    if s.count(ss) > 1:
        res = True
        break
print(res)
