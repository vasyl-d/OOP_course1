class Index:
    START_INDEX = 0

    def __init__(self, name):
        self.id = Index.START_INDEX
        Index.START_INDEX += 1
        self.name = name

    def __hash__(self):
        return hash(str(self.id))

id1 = Index("dsfas")
id2 = Index("sadg")
d = {id1: id1, id2: id2}
print(d)
print(d[id2].id)
[print(o.name, o.id) for o in d.values() if o.name=="sadg"]