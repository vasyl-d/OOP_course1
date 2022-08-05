class Model:
    def __init__(self):
        self.fields = dict()
        
    def __str__(self):
        s = "Model"
        if self.fields.keys():
            s = s + ": " + ', '.join([f"{i} = {self.fields[i]}" for i in self.fields.keys()])
        return s

    def query(self, *args, **kwargs):
        for i in kwargs.keys():
            self.fields[i] = kwargs[i]
        #или просто self.fields = kwargs


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
model2 = Model()
print(model2)