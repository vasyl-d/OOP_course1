'''Даны две строки A и B букв в нижнем регистре, верните True, если вы можете поменять местами две буквы в A так, 
чтобы результат был равен B, в противном случае верните False.

Замена букв определяется как взятие двух индексов i и j так, что i != j, и замена символов на A[i] и A[j]. 
Например, замена индексов 0 и 2 в "abcd" приводит к "cbad".'''

def a2b(a,b):
    if len(a) <2 or len(b) < 2 or len(a) != len(b):
        return False
    z = [x for x in zip(a, b) if x[0] != x[1]]
    return (len(z) == 2 and z[1] == z[0][::-1]) or (a == b[::-1])

test = [
    ('aaa aa', 'aa aaa', True),
    ('abc', 'abc',False),
    ('aba' , 'aba', True),
    ('ababa' , 'baaba', True),
    ('aifghjjhgfic' , 'cifghjjhgfia', True),
    ('aifghj jhgfi' , ' ifghjjhgfia', False),
    ('a1ifghjjhgfic' , '1aifghjjhgfi', False),
    ('asdkjfaskjfalkjf' , 'askjfhgasjfhg', False),
    ('          ' , '          ', True),
    ('    _      ' , '   _       ', True),
    ('    _      ' , '    _      ', False),
    ('aaaa    ' , 'aaaa    ', False), 
    ('' , '', False),  
    (' ' , ' ', False), 
    ('   ' , '     ', False), 
    (' фф ' , ' ф ф', True),
    ('aaaaa' , 'aaaaa', True),
    (' aaaaa ' , 'a aaa a', False),    
    ]
for x in test:
    assert a2b(x[0], x[1]) == x[2], f'error in case {x}'