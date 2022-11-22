'''Дана строка. Найдите в ней все глассные и разверни их в обратную строну.'''
s = list(input())
vowels = {'a', 'e','i', 'o', 'u', 'y'}
s2 = [_ for _ in s if _ in vowels] #list for vowels in our input

vo_ind = -1
for ind, el in enumerate(s):
    if el in vowels:
        s[ind] = s2[vo_ind] 
        vo_ind -= 1


print(''.join(s))