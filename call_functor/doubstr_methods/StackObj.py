class StackObj:
    ''' __data - ссылка на строку с переданными данными;
        __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).'''
    def __init__(self, data=""):
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

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        # - добавление объекта класса StackObj в конец односвязного списка;
        if self.top == None:
            self.top = obj
        else:
            el = self.top
            while el.next:
                el = el.next
            el.next = obj

    def pop_back(self):
        # - удаление последнего объекта из односвязного списка.
        if self.top == None:
            return
        el = self.top
        if el.next == None:
            self.top = None
            return
        while el.next.next:
            el = el.next
        el.next = None
        

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
        el = self.top
        if el == None:
            return ''
        else:
            s = el.data
            el = el.next
        while el !=None:
            s = s + ' '+ el.data
            el = el.next
        return s 

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
        

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

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
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1
    
assert i == len(d), "неверное число объектов в стеке"

st.pop_back()
assert st() == ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3'], 'не верно работает удаление pop_back()'
print(st)
l = st()
print(l)