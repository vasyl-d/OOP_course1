'''Дан список чисел nums размером n.

Верните самый часто повторяемый элемент из списка. Часто повторяемый это элемент, который появляется больше чем [n/2]'''

nums = list(map(int, input().split(',')))

unic_nums = set(nums)
freq_nums = {sum(x==n for x in nums): n for n in unic_nums}
print(freq_nums)
mk = max(freq_nums.keys())
print(mk, freq_nums[mk])

# или так: 

print(max(nums, key = nums.count))