'''класс для декоратор с параметром рендером '''
class InputValues:
    def __init__(self, render):     
        # render - ссылка на функцию или объект для преобразования
        self.render = render
        
    def __call__(self, func):     
        # func - ссылка на декорируемую функцию - она должна вернуть строку
        
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))
        return wrapper

class RenderDigit:
    '''класс для преобразования строк в целое или Ноне'''
    def __init__(self):
        pass

    def __call__(self, *args, **kwds):
        try:
            i = int(args[0])
        except ValueError:
            return None
        return i

render = RenderDigit()

#декорируем Инпут

@InputValues(render=render)
def input_dg():
    return input()

res = input_dg()
print(res)