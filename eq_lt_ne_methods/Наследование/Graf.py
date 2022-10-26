from math import inf as MAX_NUM

NUM = {int, float}

def TE(msg='Wrong type'):
    raise TypeError(msg) 

def arg_min(T, S):
    amin = -1
    m = MAX_NUM  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin

def dextra(D:list, v1, v2):
    v = 0
    N = len(D)  # число вершин в графе
    T = [MAX_NUM]*N   # последняя строка таблицы

    S = {v}     # просмотренные вершины
    T[v] = 0    # нулевой вес для стартовой вершины
    M = [0]*N   # оптимальные связи между вершинами

    while v != -1:          # цикл, пока не просмотрим все вершины
        for j, dw in enumerate(D[v]):   # перебираем все связанные вершины с вершиной v
            if j not in S:           # если вершина еще не просмотрена
                w = T[v] + dw
                if w < T[j]:
                    T[j] = w
                    M[j] = v        # связываем вершину j с вершиной v

        v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
        if v >= 0:                    # выбрана очередная вершина
            S.add(v)                 # добавляем новую вершину в рассмотрение

    # формирование оптимального маршрута:
    start = v1
    end = v2
    P = [end]
    while end != start:
        end = M[P[-1]]
        P.append(end)

    return P

class Vertex:
    __slots__ = '_links', '_num'

    def __init__(self):
        self._links = []
        self._num = 0
    
    @property
    def links(self):
        return self._links

    def connected_vertex(self):
        return [(i.v2, i.v1)[i.v2 == self] for i in self._links]

    def connected_vertex_num(self):
        return [(i.v2._num, i.v1._num)[i.v2 == self] for i in self._links]

class Link:
    __slots__ = '_v1', '_v2', '_dist'
    def __init__(self, v1:Vertex, v2:Vertex, dist=1):
        if isinstance(v1, Vertex) and isinstance(v2, Vertex):
            self._v1, self._v2, self.dist = v1, v2, dist
            if self not in v1._links:
                v1._links.append(self)
            if self not in v2._links:
                v2._links.append(self)
        else:
            TE('Must be a Vertex')

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
        return hash((self._v1, self._v2)) + hash((self._v2, self._v1))
    
    def __eq__(self, __o: object) -> bool:
        return True if hash(__o) == hash(self) else False

    def __str__(self):
        return str(self.dist)

class LinkedGraph:
    __slots__ = '_links', '_vertex'

    def __init__(self):
        self._links = {}
        self._vertex = []

    def add_vertex(self, v1:Vertex):
        if isinstance(v1, Vertex) and v1 not in self._vertex:
            self._vertex.append(v1)
            v1._num = len(self._vertex)-1        

    def add_link(self, link:Link):
        if isinstance(link, Link) and link not in self._links:
            self._links[link] = link
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def adj_mat(self):
        size = len(self._vertex)
        mat = [[MAX_NUM]*size for _ in range(size)]
        j = 0
        for v in self._vertex:
            for i in v.connected_vertex_num():
                mat[j][i] = self._links[Link(v, self._vertex[i])]._dist
            mat[j][j] = 0
            j += 1
        return mat

    def find_path(self, v1:Vertex, v2:Vertex):
        path = dextra(self.adj_mat(), v1._num, v2._num)[::-1]
        v = [self._vertex[i] for i in path]
        l = [self._links[ Link(v[i], v[i+1])] for i in range(len(v)-1)]
        return (v, l)

class Station(Vertex):
    __slots__ = 'name',
    def __init__(self, name=''):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class LinkMetro(Link):
    def __str__(self):
        return str(self.dist)

# 
map_graph = LinkedGraph()

v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
v6 = Vertex()
v7 = Vertex()

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))

print(len(map_graph._links))   # 8 связей
[print(x.v1._num, x.v2._num) for x in map_graph._links]

print(Link(v4, v5) == Link(v5, v4))
print(map_graph._links[Link(v2, v3)].v2)
print(map_graph._links[Link(v3, v2)].v2)

print(len(map_graph._vertex))  # 7 вершин
[print("Вершина: ", x._num, "Связанные: ", x.connected_vertex_num()) for x in map_graph._vertex]

[print(x) for x in map_graph.adj_mat()]

path = map_graph.find_path(v1, v6)

print("path bnwt v1 - v6: ", path[0])
[print(x._num, end = " -- ") for x in path[0]]
print()
print(map_graph._links[Link(map_graph._vertex[5], map_graph._vertex[6])])
print(map_graph._links[Link(map_graph._vertex[6], map_graph._vertex[1])])
print(map_graph._links[Link(map_graph._vertex[1], map_graph._vertex[0])])

# 
map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print("Вершин: ", len(map_metro._vertex))
print("Ребер: ", len(map_metro._links))

[print(x) for x in map_metro.adj_mat()]

path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7


# тесты

map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"