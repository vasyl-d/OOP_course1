'''Элемент, который как минимум в двараз больше остальных
В заданном целочисленном массиве nums всегда есть ровно один самый большой элемент.

Найдите, является ли самый большой элемент в массиве по крайней мере в два раза больше, чем любое другое число в массиве.

Если это так, верните индекс самого большого элемента, в противном случае верните -1.'''
res =-1
try:
    nums = [int(i) for i in  input().split(',')]
except ValueError:
    print(res)
    exit()

m1 = max(nums)
ind_m1 = nums.index(m1)
nums.pop(ind_m1)
m2 = max(nums) if len(nums) else m1/2
if m2 <= m1/2:
    res = ind_m1
print(res)