class HandlerGET:
    def __init__(self, func):
        self.__func = func


    def __call__(self, request, *args, **kwargs):
        return self.get(self.__func, request, *args, **kwargs) if request.get('method','GET') == 'GET' else None
        

    def get(self, func, request, *args, **kwargs):
        return "GET: "+self.__func(request)


@HandlerGET
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)

@HandlerGET
def index(request):
    return "главная страница сайта"

res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, f"декорированная функция вернула неверные данные res = {res}"
res = index({"method": "POST2"})
assert res is None, f"декорированная функция вернула неверные данные res = {res}"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
