class Layer:
    def __init__(self):
        self.name = "Layer"
        self.next_layer = None

    def __call__(self, obj):
        self.next_layer = obj
        return obj

class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs

class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    def __init__(self, Network):
        self.poiner = Network

    def __iter__(self):
        while self.poiner:
            yield self.poiner
            self.poiner = self.poiner.next_layer

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)

nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1
    
assert n == 4, "итератор перебрал неверное число слоев"



