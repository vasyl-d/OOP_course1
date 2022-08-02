'''использование класса-декоратора с параметрами и с функцией оберткой'''

class Handler:
    def __init__(self, methods = ('GET',)):
        self.methods = methods

    def __call__(self, func,  *args, **kwargs):
        self.__func = func
        def wrapper(request, *args, **kwargs):
            met = request.get('method','GET')
            if met in self.methods:
                if met == 'GET':
                    return self.get(self.__func, request, *args, **kwargs)
                if met == 'POST':
                    return self.post(self.__func, request, *args, **kwargs)
            return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        ''' - для имитации обработки GET-запроса'''
        return "GET: "+self.__func(request)

    def post(self, func, request, *args, **kwargs):
        ''' - для имитации обработки POST-запроса'''
        return "POST: "+self.__func(request)

#тесты
assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

#request = {"method": "POST", "url": "contact.html"}

@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"

assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

@Handler(methods=('POST'))
def index(request):
    return "index"

assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"