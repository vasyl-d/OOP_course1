'''Перевернутые цифры
X-хорошее число, если после поворота каждой цифры по отдельности на 180 градусов мы получим валидное число, отличное от X. 
Каждая цифра должна быть повернута - мы не можем оставить ее не повернутой.

Число является валидным, если каждая цифра остается цифрой после вращения. 0, 1 и 8 после поворота превращаются сами в себя; 
2 и 5 превращаются друг в друга (в этом случае они вращаются в другом направлении, другими словами, 2 или 5 зеркально отражаются); 
6 и 9 превращаются друг в друга, а остальные числа не вращаются и не превращаются ни вкакое число и становятся недействительными.

Теперь, учитывая положительное число N, сколько чисел X от 1 до N являются валидными?

Например:

Есть число 10. В диапозоне от 1 до 10 есть 4 валидных числа - 2, 5, 6, 9

Обратите внимание, что 1 и 10 не являются валидными числами, так как они остаются неизменными после вращения.'''


MGN = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}

def make_rotate(num):
    s = str(num)
    n = ''.join([MGN.get(x, 'x') for x in s])
    try:
        return(int(n))
    except ValueError:
        return(num)

n = int(input()) #вводим число больше 0
nn = [x for x in range(n+1) if x != make_rotate(x)]

print(make_rotate(171))
print(len(nn),nn)