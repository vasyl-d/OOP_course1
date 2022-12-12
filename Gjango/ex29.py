'''Longest Substring Without Repeating Characters'''
def lengthOfLongestSubstring(string: str) -> int:
    s = string
    l = len(s)
    res = s[0]
    for start in range(0, l):
        for end in range(start+1, l):
            tmp = s[start: end]

            if s[end] in tmp:
                break
            else:
                r = s[start: end+1]
                if len(r) > len(res):
                    res = r 
    return (res, len(res))


assert lengthOfLongestSubstring("asdfghjka") == ('asdfghjk',8), f"error in 1st case {lengthOfLongestSubstring('asdfghjka')}"
assert lengthOfLongestSubstring("aaasdfghjk") == ('asdfghjk',8), f"error in 2dn case {lengthOfLongestSubstring('aaasdfghjk')}"
assert lengthOfLongestSubstring("asdvvvfghjka") == ('vfghjka',7), f"error in 1st case {lengthOfLongestSubstring('asdvvvfghjka')}"

s = "hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print(lengthOfLongestSubstring(s))