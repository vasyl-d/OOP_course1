class RenderList:
    def __init__(self, type_list='ul'):
        if type_list not in {'ul','ol'}:
            self.__type_list = 'ul'
        else:
            self.__type_list = type_list

    def __call__(self, *args, **kwargs):
        rend = ''
        
        if type(args[0]) is list:
            rend = rend.join([f'<li>{i}</li>\n' for i in args[0]])
        html = f"<{self.__type_list}>\n{rend}</{self.__type_list}>" 
        return html  

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)