class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    def __init__(self, ip=0, router=None) -> None:
        self.buffer = []
        self.ip = ip
        self.router = router

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data) 
        с указанным IP-адресом получателя (пакет отправляется роутеру и 
        сохраняется в его буфере - локальном свойстве buffer);
        """
        if self.router != None:
            self.router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было, 
        то возвращается пустой список) и очищает входной буфер;
        """
        s = self.buffer
        self.buffer = []
        return s

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    def __init__(self) -> None:
        self.buffer = []
        self.dns_table = dict()
    
    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        server.ip = max(self.dns_table) + 1 if len(self.dns_table) > 0 else 1
        server.router = self
        self.dns_table.update({server.ip: server})

    
    def unlink(self,server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        if server.ip in self.dns_table:
            self.dns_table.pop(server.ip)
        server.ip = 0
            
    
    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера 
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for data in self.buffer:
            self.dns_table.get(data.ip).buffer.append(data)
        self.buffer = [] 
    

class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """
    def __init__(self, data, ip) -> None:
        self.data = data
        self.ip = ip


#пример использования
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
[print(msg.data) for msg in msg_lst_from]
[print(msg.data) for msg in msg_lst_to]