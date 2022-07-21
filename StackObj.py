class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        if type(next) == StackObj or next==None:
            self.__next = next

    def get_last(self):
        if self.next == None:
            return self
        else:
            return(self.next.get_last())
    
class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, obj): #- добавление объекта класса StackObj в конец односвязного списка;
        if type(obj) == StackObj:
            if self.top == None:
                self.top = obj
                obj.next = None
            else:
                last = self.top if self.top.next == None else self.top.get_last()
                last.next = obj
                obj.next = None
        
    def pop(self): # - извлечение последнего объекта с его удалением из односвязного списка;
        if self.top != None:
            it = self.top
            if it.next == None:
                last = it
                self.top = None
            else:
                while it.next.next != None:
                        it = it.next
                last = it.next
                it.next = None
        else:
            last = None
        return last

    def get_data(self): # - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления).
        s = []
        if self.top != None:
            it = self.top
            s = s + [it.data]
            while it.next != None:
                it = it.next
                s = s + [it.data]
        return s

st = Stack()
st.push(StackObj("obj1"))
#st.push(StackObj("obj2"))
#st.push(StackObj("obj3"))
print(st.pop().data)
res = st.get_data()
print(*res)