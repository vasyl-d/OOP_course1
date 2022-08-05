class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj:ObjList):
        if self.tail is None:
            # empty list
            self.tail = obj
            obj.next = None
            self.head = obj
            obj.prev = None
        else:
            obj.prev = self.tail
            obj.next = None
            self.tail.next = obj
            self.tail = obj
        

    def remove_obj(self, indx):
        '''удалет элемент из списка по индексу'''
         # empty list
        if self.tail == None:
            self.head = None
            return None
        if indx == 0:
            # 1 только один элемент
            if self.tail.next == None:
                s = self.tail
                self.head = None
                self.tail = None
                return s
            s = self.head
            self.head.next.prev = None
            self.head = self.head.next
            return s

        obj = self.head
        i = 0
        while obj:
            i+=1
            obj = obj.next
            if i == indx:
                break
            elif i > indx:
                return None
              
        obj.prev.next = obj.next
        if obj.next != None:
            #middle of list
            obj.next.prev = obj.prev
        else:
            #end of list
            self.tail = obj.prev 
        return obj


    def __len__(self):
        '''возвращает кол-во элементов'''
        i = 0
        obj = self.head
        while obj:
            i += 1
            obj = obj.next
        return i

    def __call__ (self, indx):
        '''возвращает содержимое data элемента списка по индексу'''
        obj = self.head
        i = 0
        while obj:
            if i == indx:
                return obj.data
            elif i>indx:
                return None
            i += 1
            obj = obj.next
        

    def __str__ (self):
        obj = self.head
        s = ''
        while obj:
            s += obj.data
            obj = obj.next
        return s

    def prn_ms(self):
        obj = self.tail
        s = ''
        while obj:
            s += obj.data
            obj = obj.prev
        return s


#проверки

ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
print(ln)
print(ln.prn_ms())
ln.remove_obj(2)
print(ln)
print(ln.prn_ms())
ln.add_obj(ObjList("Python 2"))
print(ln)
ln.remove_obj(2)
assert len(ln) == 2, f"функция len вернула неверное число объектов в списке {len(ln)}, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("2 Python 2"))
print(ln)
assert ln(2) == "2 Python 2", f"неверное значение атрибута __data {ln(2)}, взятое по индексу"
assert len(ln) == 3, f"функция len вернула неверное число объектов в списке {len(ln)}"
assert ln(1) == "Балакирев", f"неверное значение атрибута __data {ln(1)}, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"