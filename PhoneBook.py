class PhoneNumber:
    '''number - номер телефона (число);
        fio - ФИО владельца номера телефона.'''
    def __init__(self, number:int, fio:str) -> None:
        self.fio = fio
        if self.is_num(number):
            self.number = number
        else:
            raise Exception('Not valid format of phone number')

    @staticmethod
    def is_num(number):
        return True if 9999999999 < number <= 99999999999 else False
    
class PhoneBook:
    def __init__(self) -> None:
        self.book = []

    def add_phone(self, phone:PhoneNumber):
        ''' - добавление нового номера телефона (в список);
        '''
        self.book += [phone]

    def remove_phone(self, indx:int):
        ''' - удаление номера телефона по индексу списка;'''
        if 0 <= indx <= len(self.book):
            self.book.pop(indx)
        else:
            raise Exception('Invalid index')

    def get_phone_list(self):
        ''' - получение списка из объектов всех телефонных номеров.'''
        return self.book


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
[print(f"{i.fio} : {i.number}") for i in phones]