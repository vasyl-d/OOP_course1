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
    if s % 3 != 0: 
        print('not %3')
        return False
    res = []
    part = s / 3
    start = 0
    end = 1
    j = 0
    l = len(arr)

    while end <= l: 
        if j < 2:
            s = arr[start:end]
            if sum(s) == part:
                res.append(s)
                start = end 
                j += 1
            end = end + 1
        else:
            break
    if arr[start:]:    
        res.append(arr[start:])
    print(res)
    return(all(map(lambda x: sum(x)==part, res)) and len(res) == 3)

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
        ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], True),

    ]
    for x in test:
        assert check_split3(x[0])==x[1], f"Error in Test {x}"
    return('OK')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print('testing')
        print(test_())
    else:
        arr = [int(i) for i in  input().split(',')]
        print(check_split3(arr))
