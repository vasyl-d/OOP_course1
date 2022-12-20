'''Дан массив a неотрицательных целых чисел, верните массив, состоящий из всех четных элементов a, за которыми следуют все нечетные элементы a.

Вы можете вернуть любой массив ответов, удовлетворяющий этому условию. Порядок неважен.'''
import time 

nums = list(map(int, input().split(',')))

t1 = time.time()
chet = list(filter(lambda x: x%2 == 0, nums))
chet.extend(list(filter(lambda x: x%2 != 0, nums)))
print(chet)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
res = []
for i in nums:
    if i % 2 == 0:
        res = [i] + res
    else:
        res = res + [i]
print(res)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
print(sorted(nums, key=lambda x: x % 2 != 0))
t2 = time.time()
print(t2 - t1)
