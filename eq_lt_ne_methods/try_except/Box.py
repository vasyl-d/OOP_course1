class Box:
    '''_name - ссылка на параметр name;
    _max_weight - ссылка на параметр max_weight;
    _things - список из вещей, хранящиеся в ящике (изначально пустой список).'''
    __slots__ = ('_name', '_max_weight', '_things')
    def __init__(self, name=None, max_weight=0) -> None:
        self._name, self._max_weight, self._things = name, max_weight, []

    def add_thing(self, obj):
        pass
