'''reversing int number in range 2^31-1 '''

x = int(input())

x2 = int(str(x)[::-1]) if x >= 0 else -int(str(abs(x))[::-1]) 
x2 = x2 if abs(x2) <= (2**31)-1 else 0
print(x2)