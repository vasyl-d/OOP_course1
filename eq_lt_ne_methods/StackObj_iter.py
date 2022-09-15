class StackObj:
    ''' __data - ссылка на строку с переданными данными;
        __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).'''
    def __init__(self, data=""):
        self.__data, self.__next = data, None

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

    def __str__(self):
        return str(self.data)

    def prn2end(self):
        if self.next == None:
            return str(self.data)
        else:
            return str(self) + ' ' + self.next.prn2end()

    def count2end(self):
        return 1 if self.next == None else 1 + self.next.count2end()  
        

class Stack:

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        # - добавление объекта класса StackObj в конец односвязного списка;
        if self.top:
            self.top.get_last().next = obj
        else:
            self.top = obj

    def push_front(self, obj:StackObj):
        # - добавление объекта класса StackObj в конец односвязного списка;
        if self.top:
            obj.next = self.top
            self.top = obj
        else:
            self.top = obj

    def pop(self):
        # - удаление последнего объекта из односвязного списка.
        if self.top == None:
            return None
        el = self.top
        if el.next == None:
            self.top = None
            return self.top
        while el.next.next:
            el = el.next
        e = el.next
        el.next = None
        return e     

    def __add__(self, other):
        if type(other) == StackObj:
            self.push_back(other)
        return self

    def __radd__(self, other):
        return self.__sum__(other)

    def __mul__(self, other):
        if type(other) == list:
            for el in other:
                self.push_back(StackObj(el))
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return self.top.prn2end() if self.top else " "
            
    def __call__(self, *args, **kwds):
        el = self.top
        s = []
        if el == None:
            return s
        else:
            s = [el.data]
            el = el.next
        while el !=None:
            s = s + [el.data]
            el = el.next
        return s 
    
    def __len__(self):
        return self.top.count2end()

    def check(self, key:int):
        if type(key) is int and 0 <= key < len(self):
            return key
        raise IndexError('неверный индекс')

    def __getitem__(self, key:int):
        key = self.check(key)
        el = self.top
        i = 0
        while i < key:
            el = el.next
            i += 1
        return el.data

    def __setitem__(self, key:int, value:str):
        key = self.check(key)
        el = self.top
        i = 0
        while i < key:
            el = el.next
            i += 1
        el.data = value

    def insert_item(self, key:int, value:StackObj):
        # insert into middle of stack by index
        key = self.check(key)
        el = self.top
        i = 0
        while i < key:
            prev = el
            el = el.next
            next = el.next if el.next is not None else None
            i += 1
        el = value
        prev.next = el
        el.next = next            

    def __iter__(self):
        el = self.top
        while el:
            yield el
            el = el.next

assert hasattr(Stack, 'pop'), "класс Stack должен иметь метод pop"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
print(st)
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1
    
assert i == len(d), "неверное число объектов в стеке"

st.pop()
assert st() == ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3'], 'не верно работает удаление pop()'
print(st)
print(len(st))
l = st()
print(l)
print(st()[0])
print(st[0])

st[1] = StackObj("sdfgsdfg")
print(st[1])
print(st)

#tests

st2 = Stack()
st2.push_back(StackObj("obj11"))
st2.push_back(StackObj("obj12"))
st2.push_back(StackObj("obj13"))
print(st2)
st2[1] = StackObj("obj2-new")
print(st2)
print(st2[0])
print(st2[1])

# assert st2[0] == "obj11" and st2[1] == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st2[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st2.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st2.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next
    
assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"