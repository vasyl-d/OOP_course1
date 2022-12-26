'''В колоде карт на каждой карте записано целое число.

Верните True тогда и только тогда, когда вы можете выбрать X >= 2 таким образом, 
чтобы можно было разделить всю колоду на 1 или более групп карт, где:

Каждая группа имеет ровно X карт.
Все карты в каждой группе имеют одно и то же целое число.
Пример:

deck = [1,2,3,4,4,3,2,1]
True

Есть возможность разделить карты на 4 группы [1,1],[2,2],[3,3],[4,4].'''

nums = list(map(int, input().split(',')))

def is_group(nums):
    freq = {n: nums.count(n) for n in nums}
    f = freq.values()
    min_freq = min(f)
    max_freq = max(f)

    if min_freq < 2:
        return False

    # find max common divider 
    for i in range(min_freq, 1, -1):
        if all(map(lambda x: x%i == 0, f)):
            return True
    return False

print(is_group(nums))

tests = [([1,2,3,4,4,3,2,1], True),
        ([1, 1, 2, 2, 2, 2], True),
        ([1, 1, 1, 1, 2, 2, 2, 2, 2, 2], True),
        ([0, 0, 0, 0, 1, 1, 2, 2, 3, 3], True),
        ([1,2,3,4,5,6], False),
        ([1,1,2,2,3,3,3], False),
]

for t in tests:
    assert is_group(t[0]) == t[1], f"Error in test {t}"



