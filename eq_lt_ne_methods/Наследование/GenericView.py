class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return "get"

    def post(self, request):
        return "post"

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)
    
    def check_request(self, request):
        if type(request) is dict:
            if 'url' in request:
                 return(request)
            else:
                raise TypeError('request не содержит обязательного ключа url')
        else:
            raise TypeError('request не является словарем')

    def get(self, request):
        return f"url: {self.check_request(request)['url']}"

    def render_request(self, request, method):
        if method in self.methods:
            return getattr(self, method.lower())(request)
        else:
            raise TypeError('данный запрос не может быть выполнен')

dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
print(html)