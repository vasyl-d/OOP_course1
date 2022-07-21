class AppStore:
    """Объявите класс AppStore - интернет-магазин приложений для устройств 
    под iOS. В этом классе должны быть реализованы следующие методы:
    """
    def __init__(self) -> None:
        self.app_list = set()

    def add_application(self, app):
        """добавление нового приложения app в магазин
        """
        if app not in self.app_list:
            self.app_list.add(app)

    def remove_application(self, app):
        """удаление приложения app из магазина
        """
        self.app_list.discard(app)
    
    def block_application(self, app):
        """блокировка приложения app (устанавливает локальное
        свойство blocked объекта app в значение True)
        """
        app.blocked = True
    
    def total_apps(self):
        """возвращает общее число приложений в магазине
        """
        return len(self.app_list)


class Application:
    """Здесь Application - класс, описывающий добавляемое приложение 
    с указанным именем. Каждый объект класса Application должен содержать 
    локальные свойства:
    name - наименование приложения (строка);
    blocked - булево значение (True - приложение заблокировано;
    False - не заблокировано, изначально False).
    Как хранить список приложений в объектах класса AppStore решите сами.
    """
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
