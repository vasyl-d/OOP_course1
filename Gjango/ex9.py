'''find a good series of days to buy and sell in a period'''

inp_list = list(map(int, input().split(','))) # comma separeted list of prices


def findMaxProfit(price):
    days = []
    # следит за максимальной полученной прибылью
    profit = 0
 
    # инициализирует локальный минимум индексом первого элемента
    j = 0
 
    # старт со второго элемента
    for i in range(1, len(price)):
 
        # обновляет локальный минимум, если найдена убывающая последовательность
        if price[i - 1] > price[i]:
            j = i
 
        # продаеv, если текущий элемент является максимумом', т.е.
        # (`previous <= current > next`)
        if price[i - 1] <= price[i] and (i + 1 == len(price) or price[i] > price[i + 1]):
            profit += (price[i] - price[j])
            days.append((j + 1, i + 1))
    return profit, days

print(findMaxProfit(inp_list)[0])

# есть и такой вариант: 
# print(sum([a[i]-a[i-1] for i in range(1, len(a)) if a[i] > a[i-1]]))