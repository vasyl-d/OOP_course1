class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return list(map(int, self.func().split()))
        
#декоратор для Инпута    
input_dg = InputDigits(input)
res = input_dg()
# а можно так:
#@InputDigits
#def input_dg():
#    return input()
print(res)