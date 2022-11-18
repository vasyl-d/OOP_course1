'''Romanian to arab number '''

control = [
    (1000, 'M', 1),
    (900, 'CM', 2),
    (500, 'D', 1),
    (400, 'CD', 2),
    (100, 'C', 1),
    (90, 'XC', 2),
    (50, 'L', 1),
    (40, 'XL', 2),
    (10, 'X', 1),
    (9, 'IX', 2),
    (5, 'V', 1),
    (4, 'IV', 2),
    (1, 'I', 1)]


def toInteger(num:str):
    result, offset = 0, 0
    for c, r, l in control:
        while num[offset:].startswith(r):
            # print(f"{num[offset:]} start with {r}")
            result += c
            offset += l
    return result
    



# n = 'MCMI'
# print(n, toInteger(n))
# n = 'MCMVI'
# print(n, toInteger(n))
# n= 'MCMII'
# print(n, toInteger(n))

# n = 'III'
# print(n, toInteger(n))

# n = 'MCIX'
# print(n, toInteger(n))
# n = 'XXIV'
# print(n, toInteger(n))

n= 'CXCIX'
print(n, toInteger(n))





