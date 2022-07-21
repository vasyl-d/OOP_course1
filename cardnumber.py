from string import ascii_lowercase, digits
from re import match

CHARS_FOR_NAME = set(ascii_lowercase.upper() + digits+' ')

class CardCheck:
    def __init__(self, number, name):
        if self.check_card_number(number) and self.check_name(name):
            self.name = name
            self.number = number
    
    @staticmethod
    def check_card_number(number): # проверяет строку с номером карты и возвращает булево значение True, если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
        return True if match('\d{4}-\d{4}-\d{4}-\d{4}', number) else False

    @staticmethod
    def check_name(name): # проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно и False - в противном случае.
        return True if match('[1-9A-Z]+ [1-9A-Z]+$', name) else False

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name, is_number)