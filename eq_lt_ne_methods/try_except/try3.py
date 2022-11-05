a, b = input().split()
try:
    sum = int(a)+int(b)
except ValueError:
    try:
        sum = float(a)+float(b)
    except ValueError:    
        sum = str(a) + str(b)
finally:
    print(sum)