'''Изменить массив A в соответствии с числом K
Для неотрицательного целого числа X форма массива X представляет собой массив его 
цифр в порядке слева направо. Например, если X = 1231, то форма массива равна [1,2,3,1].

Дан массив a - неотрицательного целого числа х, верните массив целого числа х+к.

Пример:

A = [1,2,0,0], K = 34
[1,2,3,4]
1200 + 34 = 1234'''

def arr2str(arr):
    try:
        return ''.join([str(x) for x in arr])
    except ValueError:
        return ''

def arr2num(arr):
    try:
        return int(arr2str(arr))
    except ValueError:
        return 0

def K_arr(nums, k):
    n = arr2num(nums) + k
    try:
        return [int(_) for _ in str(n)]
    except ValueError:
        return []

try:
    nums = list(map(int, input().split(',')))
except ValueError:
    nums = []

try:
    k = int(input())
except ValueError:
    k = 0

res = K_arr(nums, k)
print(res)


test = [
    ([1,2,0,0], 34, [1, 2, 3, 4]),
    ([1,2,0,0], 0, [1, 2, 0, 0]),
    ([], 0, [0])
]


for x in test:
    assert K_arr(x[0], x[1]) == x[2], f"Error in test {x}"