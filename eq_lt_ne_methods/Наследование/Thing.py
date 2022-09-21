class Thing:
    __instance_count = 1

    def __init__(self, name, price):
        # id, name, price, weight, dims, memory, frm
        self.name, self.price = name, price
        self.weight, self.dims, self.memory, self.frm = None, None, None, None
        self.id = Thing.__instance_count
        Thing.__instance_count += 1
    
    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)

class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight, self.dims = weight, dims

class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory, self.frm = memory, frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
print(table.__dict__)
print(book.__dict__)