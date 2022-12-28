'''Найдите общую букву
Дан массив a строк, составленных только из строчных букв, верните упорядоченый список всех символов, 
которые отображаются во всех строках в списке (включая дубликаты).'''
import sys

def res_common_let(a):
    # выделил общие уникальные буквы, сделал их частоты по словам и вывел в списк с минимальной частотой. отсортировал
    uniq_common_leters = set(a[0])

    for i in range(1, len(a)):
        uniq_common_leters.intersection_update(set(a[i]))

    dict_3 = {l:{w.count(l) for w in a} for l in uniq_common_leters}

    res = []
    for el in dict_3.keys():
        res.extend([el]*min(dict_3[el]))

    return sorted(res)

def test_():
    test = [
        (['asdfa', 'sfhgjgj', 'asfkjl;knv'], ['f','s']),
        (['', 'sdgsd', 'sdrgfsd'], []),
        (['sdfgsd4', '1111', 'aesdfgbv'],[])
    ]
    
    try:
        for x in test:
            assert res_common_let(x[0]) == x[1], f"Error in test {x}"
    except Exception as e:
        return(f"Error: {e}")

    return("OK")


if __name__ == '__main__':
    if sys.argv[1] == 'test':
        print('testing')
        print(test_())
    else:
        a = [i for i in  input().split(',')]
        print(res_common_let(a))

