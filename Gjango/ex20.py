'''Дан целочисленный массив nums, найдите три числа, произведение которых является максимальным, и верните максимальное произведение.'''

nums = sorted(list(map(int, input().split(','))))
s = 1
l = nums[-3:]
for x in l:
    s = s * x
# a,b,c = nums[:3]
# print(a*b*c)
print(l, 'mul:', s)