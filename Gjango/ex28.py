import time

'''median of 2 arrays'''
def findMedianSortedArrays(nums1, nums2) -> float:
    nums1.extend(nums2)
    nums = sorted(nums1)
    n = len(nums) //2
    return (nums[n-1]+nums[n])/2 if len(nums)%2 == 0 else nums[n]

'''longest polindromic substring'''
def longestPalindrome(s: str) -> str:

    l = len(s)
    res = ''
    for frame in range(l, 0, -1):
        x = l - frame + 1
        for ind in range(0, x):
            test = s[ind:ind+frame]
            if test == test[::-1]:
                res = test
                return res 
    return res

def longestPalindrome2(s):
    """
    :type s: str
    :rtype: str
    is x500 times faster than 1st one case
    """
    longest = ""
    maxLength= 1
    start = 0
    low = 0
    high = 0
    string = s
    length = len(s)
    for i in range(1, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1

        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1
        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

    return string[start:start + maxLength]

assert longestPalindrome2('asdad') == 'dad', "не верно в кейсе 1"
assert longestPalindrome2('dad') == 'dad', "не верно в кейсе 2"
assert longestPalindrome2('dadaassa') == 'assa', f"не верно в кейсе 3, {longestPalindrome2('dadaassa')}"
assert longestPalindrome2("babad") == 'bab', f"не верно в кейсе 3, {longestPalindrome2('babad')}"
assert longestPalindrome2("ba") == 'b', f"не верно в кейсе 3, {longestPalindrome2('ba')}"
assert longestPalindrome2("a") == 'a', f"не верно в кейсе 3, {longestPalindrome2('a')}"
s = "wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"

tm = time.time()
print(longestPalindrome2(s))
tm2 = time.time()
print(tm2 - tm)
