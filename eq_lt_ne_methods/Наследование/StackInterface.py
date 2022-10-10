from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        #  - добавление объекта в конец стека;
        pass

    @abstractmethod
    def pop_back(self):
        #  - удаление последнего объекта из стека.
        pass

class StackObj:
    def __init__(self, data=' ', next=None):
        self._data, self._next = data, next

    def __str__(self):
        return str(self._data)

class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def __iter__(self):
        el = self._top
        while el:
            yield el
            el = el._next

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            *_, last = self 
            last._next = obj

    def pop_back(self):
        if self._top is None:
            return None
        if self._top._next is None:
            last = self._top
            self._top = None
            return last

        # if __iter__ is defined:
        # *_, p_last, last = self
        # splits iterable into 3 entities

        *_, p_last, last = self
        p_last._next = None
        return last

    def __str__(self):
        return '\n'.join([str(el) for el in self])
# 
st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
print(st)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print("deleted: ", del_obj)
[print(el) for el in st]
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print("deleted: ", del_obj)
[print(el) for el in st]
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print("deleted: ", del_obj)
[print(el) for el in st]