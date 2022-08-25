import sys

class MailBox:
    def __init__(self, *args):
        self.inbox_list = args if args else []

    def receive(self):
        #lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
                'Python ООП; Балакирев С.М.; 2022',
                'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        self.inbox_list = [MailItem(*el.split('; ')) for el in lst_in]
        

class MailItem:
    ''' mail_from - email отправителя (строка); title - заголовок письма (строка), content - содержимое письма (строка)'''
    def __init__(self, mail_from, title, content):
        self.is_read = False
        self.mail_from = mail_from
        self.title = title
        self.content = content

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read
    
    def __str__(self) -> str:
        return f"Отправитель: {self.mail_from}, заголовок: {self.title}"

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
[print(el) for el in inbox_list_filtered]
