'''Дан массив чисел. Найдите и верните 3е максимальное число. Если третье максимальное не существует, то верните самое большое число.

Например в массиве nums = [3, 2, 1] максимальное число 3, после него 2, а третье максимальное 1.

'''
nums = set(map(int, input().split(',')))
sn = sorted(list(nums))
try:
    print(sn[-3])
except IndexError:
    print(sn[-1])
