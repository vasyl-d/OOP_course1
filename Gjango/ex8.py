'''find a good day to buy and sell in a period'''

inp_list = list(map(int, input().split(','))) # comma separeted list of prices

value, d1, d2 = 0, 0, 0
l = len(inp_list)
for i, v in enumerate(inp_list):
    for j in range(i+1, l):
        diff = inp_list[j] - v
        if diff > value:
             value = diff
             d1 = i
             d2 = j

print(value, d1, d2)
