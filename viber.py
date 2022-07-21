class Viber:
    msg_set = []

    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений;
        """
        if msg not in cls.msg_set:
            cls.msg_set.append(msg)

    @classmethod
    def remove_message(cls, msg):
        """удаление сообщения из списка;
        """
        if msg in cls.msg_set:
            cls.msg_set.remove(msg)

    @classmethod
    def set_like(cls, msg):
        """поставить/убрать лайк для сообщения msg 
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        if msg in cls.msg_set:
            msg.fl_like = not msg.fl_like
    
    @classmethod
    def show_last_message(cls, n):
        """отображение последних сообщений;
        """
        l = len(cls.msg_set)
        if n > l:
            n = l
        return cls.msg_set[-n::]

    @classmethod
    def total_messages(cls):
        """звращает общее число сообщений.
        """
        return len(cls.msg_set)

class Message:
    """позволяет создавать объекты-сообщения со следующим 
    набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения 
    (булево значение True - если лайк есть и False - в противном 
    случае, изначально False);
    """
    def __init__(self, text, fl_like=False) -> None:
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
[print(i.text) for i in Viber.show_last_message(2)]