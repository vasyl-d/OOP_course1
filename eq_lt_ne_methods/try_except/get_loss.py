def get_loss(w1, w2, w3, w4):
    # где w1, w2, w3, w4 - любые числа. Функция должна возвращать значение, вычисленное по формуле:
    try:
        w1 // w2
    except:
        return("деление на ноль")
    else:
        return 10 * w1 // w2 - 5 * w2 * w3 + w4

print(get_loss(1,2,2,3))