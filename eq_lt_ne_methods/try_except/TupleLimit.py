class TupleLimit(tuple):
    '''when we do nest from immutable object/like tuple - then we need to overwrite __new__ method'''
    def __new__(cls, _iterable, max_length):
        if not iter(_iterable) or type(max_length) is not int:
            raise TypeError("Must be an iterable and int")
        
        if len(_iterable) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')

        return super(TupleLimit, cls).__new__(cls, _iterable)

    def __repr__(self) -> str:
        return ' '.join(map(str, self))

try:
    digits = list(map(float, input().split()))
    tp = TupleLimit(digits, 5)
    print(tp)
except Exception as e: 
    print(e)