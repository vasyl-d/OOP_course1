'''Дан массив чисел nums. Найди в этом массиве нули и подвинь их в конец. Остальные числа должны идти в том же порядке.'''
nums =[]
while True:
    try:
        nums = list(map(int, input().split(',')))
    except (ValueError, TypeError):
        pass
    else:
        break

n = list(filter(lambda x: x !=0, nums))
s2 = len(nums) - len(n) # or nums.count(0)
n2 = [0]*(s2)
n = n + n2
print(n)

# или просто так: 
# sorted(nums, key=bool, reverse=True)

