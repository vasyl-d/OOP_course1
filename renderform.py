from string import ascii_lowercase, digits
CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
CHARS_CORRECT_SET = set(CHARS_CORRECT)

# здесь объявляйте классы TextInput и PasswordInput
class Input_():
    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size
    
    @classmethod
    def check_name(cls, name):
        fl = True
        if len(name) > 50 or len(name) <3:
            fl = False
        if not CHARS_CORRECT_SET.issuperset(set(name.lower())):
            fl = False
    
        if not fl:
            raise ValueError("некорректное поле name")
        return fl

class TextInput(Input_):
    def get_html(self): # возвращает сформированную HTML-строку в формате:
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

class PasswordInput(Input_):
     def get_html(self): # возвращает сформированную HTML-строку в формате:
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)