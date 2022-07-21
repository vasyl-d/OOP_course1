class LinkedList:
    """объявите класс LinkedList, который будет представлять связный список в целом 
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """
    def __init__(self, head =None, tail=None) -> None:
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;
        """
        if self.head == None:
            self.head = obj
        obj.set_next(None)
        obj.set_prev(self.tail)
        if self.tail != None:
            self.tail.set_next(obj)
        self.tail = obj

    def remove_obj(self):
        """удаление последнего объекта из связного списка;
        """
        if self.tail != None:
            obj = self.tail.get_prev()
            if obj != None:
                obj.set_next(None)
                self.tail = obj
            else:
                self.head = None
                self.tail = None

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.
        """
        data = []
        if self.head == None:
            return []
        obj = self.head
        data.append(obj.get_data())
        nxt = obj.get_next()
        while nxt != None:
            data.append(nxt.get_data())
            nxt1 = nxt.get_next()
            nxt = nxt1
        #data.append(self.tail.get_data())
        return data
        

class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
    """
    def __init__(self, data, prev=None, next=None) -> None:
        self.set_prev(prev)
        self.set_next(next)
        self.set_data(data)

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj;
        """
        self.__next = obj
    
    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj;
        """
        self.__prev = obj
    
    def get_next(self):
        """получение значения приватного свойства __next;
        """
        return self.__next
    
    def get_prev(self):
        """получение значения приватного свойства __prev;
        """
        return self.__prev
    
    def set_data(self, data):
        """изменение приватного свойства __data на значение data;
        """
        self.data = data
    
    def get_data(self):
        """получение значения приватного свойства __data.
        """
        return self.data
    

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
#lst.add_obj(ObjList("данные 3"))
#lst.add_obj(ObjList("данные 4"))
#lst.add_obj(ObjList("данные 5"))
print(lst.get_data()) 
lst.remove_obj()
print(lst.get_data())