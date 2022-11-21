'''Дан массив чисел nums и число k. Определите есть ли в массиве такие числа дубликаты, чтобы между ними было расстояние k.'''
while True:
    try:
        nums = list(map(int, input().split(',')))
        k = int(input())
    except (ValueError, TypeError):
        pass
    else:
        break
# print(f"k: {k}, nums: {nums}")
print(any(nums[el] == nums[el+k+1] for el in range(len(nums)-k)))