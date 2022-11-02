def str2num(s):
    try:
        i = int(s)
        return i 
    except:
        try:
            i = float(s)
            return i
        except:
            pass
    return s
    
# 1 -5.6 True abc 0 23.56 hello
lst_in = input().split()
lst_out = list(map(str2num, lst_in))
print(lst_out)