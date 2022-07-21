class SingletonFive:
    __instance_count = 0
    __instance_id = None
    # создаем только 5 об'ектів классу
    # все что более 5 - ссілается на 5й елемент.
 
    def __new__(cls, *args, **kwargs):
        if cls.__instance_count < 5:
            cls.__instance_count +=1
            cls.__instance_id = super().__new__(cls)
        return cls.__instance_id

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
[print(i.name) for i in objs]