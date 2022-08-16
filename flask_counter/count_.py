NUM = {int, float}

class Counter:
    __instance_id = None
    counter = dict()
    def __new__(cls, *args, **kwargs):
        if cls.__instance_id == None:
            cls.__instance_id = super().__new__(cls)
        return cls.__instance_id
    
    def __init__(self, *args):
        if args:
            self.counter[args[0]] = 0

    def add_counter(self, name, value):
        if type(value) in NUM:
            if name in self.counter:
                self.counter[name] += value
            else:
                self.counter[name] = value
    
    def pop_counter(self, name):
        if name in self.counter:
            self.counter.pop(name)

    def get_counter(self, name):
        if name in self.counter:
            return self.counter[name]
        return None

cl = Counter('One')
cl2 = Counter('Two')
cl.add_counter('One', 200)
print(cl.counter)
print(cl.get_counter('One'))
cl.pop_counter('One')
print(cl.counter)

