'''Дан массив nums = [3,0,1]. n = 3. В массиве 3 числа в диапозоне от 0 до 3 включительно пропущено число 2.'''

while True:
    try:
        nums = list(map(int, input().split(',')))
    except (ValueError, TypeError):
        pass
    else:
        break

s = set(range(min(nums), len(nums)+1))
print(*(s - set(nums)))