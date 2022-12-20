'''Массив монотонен, если он либо монотонно увеличивается, либо монотонно уменьшается.

Массив A монотонно увеличивается, если для всех i <= j, A[i] < = A[j]. Массив A монотонно убывает, если для всех i <= j, A[i] >= A[j].

Верните True тогда и только тогда, когда данный массив A монотонен.'''
def monoton_gt(nums):
    if not nums:
        return False
    gt = True if nums[0] <= nums[-1] else False
        
    for ind in range(1, len(nums)):
        if gt:
            if nums[ind] < nums[ind-1]:
                return(False)
        else:
            if nums[ind] > nums[ind-1]:
                return(False)            
    return True

try:
    nums = list(map(int, input().split(',')))
except ValueError:
    print(False)
else:
    print(monoton_gt(nums))


assert monoton_gt([1,2,2,3]) == True, 'не верно в 1 кейсе'
assert monoton_gt([2,2,2,1]) == True, 'не верно в 2 кейсе'
assert monoton_gt([-10,-2,2,3]) == True, 'не верно в 3 кейсе'
assert monoton_gt([-10]) == True, 'не верно в 4 кейсе'
assert monoton_gt([]) == False, 'не верно в 5 кейсе'
assert monoton_gt([9,8,7,7,2]) == True, 'не верно в 4 кейсе'
