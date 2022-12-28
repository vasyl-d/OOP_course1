'''Дан массив целых чисел arr, верните True, если мы можем разбить массив на три непустые части с равными суммами.

Формально мы можем разбить массив, если сможем найти индексы i + 1 < j с помощью 

(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j-1] == arr[j] + arr[j + 1] + ... + arr[arr. length - 1])

Пример:

arr = [0,2,1,-6,6,-7,9,1,2,0,1]
True
0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1'''
import sys

def check_split3(arr):
    s = sum(arr)
    if s % 3 != 0: return False
    res = [0,0,0]
    part = s / 3
    i = 0
    j = 0
    l = len(arr)
    while j < l:
        if i > 3: return False
        while res[i] < part and j < l:
            res[i] += arr[j]
            j += 1
        i += 1
    return(all(map(lambda x: x==part, res)))

def test_():
    test = [
        ([0,2,1,-6,6,-7,9,1,2,0,1], True),
        ([0,2,1,0,0,0,3,1,2,0,0], True),
        ([0,2,7,0,0,0,0,0,0,0,0], False),
        ([0,2,7,2,7,0,2,7,0,2,7], False),
        ([0,1,1,0,0,1,1,0,1,1,0], True),
        ([9,0,-6,0,0,1,1,0,1,-6,0], False),
        ([1,2,3], False),
        ([], False),
        ([0,0,0], True),
        ([3,3,3], True),
        ([-12,0,24], False),
        ([-12,0,12], False),
    ]
    return('OK')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print('testing')
        print(test_())
    else:
        arr = [int(i) for i in  input().split(',')]
        print(check_split3(arr))