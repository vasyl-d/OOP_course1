class Appl:
    def __init__(self, name = ''):
        self.name = name

class AppVK(Appl):
    def __init__(self):
        super().__init__('ВКонтакте')

class AppYouTube(Appl):
    def __init__(self, memory_max = 1024):
        super().__init__('YoyTube')
        self.memory_max = memory_max

class AppPhone(Appl):
    def __init__(self, phone_list=dict()):
        super().__init__("Phone")
        self.phone_list = phone_list

class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, obj):
        if type(obj) not in set(map(type, self.apps)):
            self.apps.append(obj)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
ap = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112})
sm.add_app(ap)
for a in sm.apps:
    print(a.name)
sm.remove_app(ap)
for a in sm.apps:
    print(a.name)