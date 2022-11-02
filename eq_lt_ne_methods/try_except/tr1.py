def str2int(s:str):
    try:
        res = int(s)
        return res
    except:
        return 0

# 8 11 abcd -7.5 2.0 -5
lst_in = input().split()
out = sum(map(int, filter(str2int, lst_in)))
print(out)

# or

out = sum(map(str2int, lst_in))
print(out)
