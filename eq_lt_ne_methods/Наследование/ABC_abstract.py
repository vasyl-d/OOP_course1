from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"

class ModelForm(Model):
    def __init__(self, login, password):
        self._login, self._password, self._id = login, password, id(self)

    def get_pk(self):
        return self._id

form = ModelForm("Логин", "Пароль")
print(form.get_pk())