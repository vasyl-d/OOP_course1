NUM = {int, float}

def TE(msg):
    raise TypeError(msg)

class Link:
    __slots__ = '_v1', '_v2', '_dist'
    def __init__(self, v1:int, v2:int, dist=1):
        if isinstance(v1,int) and isinstance(v2,int):
            self._v1, self._v2, self.dist = v1, v2, dist
        else:
            TE('Must be a:int')

    @property
    def v1(self):
        return self._v1
    
    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value if type(value) in NUM else TE('Must be a number')

    def __hash__(self) -> int:
        return hash(self._v1) + hash(self._v2)
    
    def __eq__(self, __o: object) -> bool:
        return True if hash(__o) == hash(self) else False

l1 = Link(1,1, 1)
l2 = Link(2,2, 1)

links = {l1:l1, l2:l2}


print(links[l1].v1)
print(Link(1,1,1) in links)
