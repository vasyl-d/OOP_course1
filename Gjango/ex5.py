'''len of last word in line or 0'''
s = input().split()
print(len(s[-1]) if len(s) != 0 else 0)
