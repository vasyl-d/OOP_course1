class DataBase:
    '''path - путь к файлу с данными БД (строка).'''
    dict_db: dict

    def __init__(self, path='') -> None:
        self.dict_db = dict()
        self.path = path

    def write(self, record):
        # - для добавления нвой записи в БД, представленной объектом record;
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]

    def read(self, pk):
        # - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое положительное число); 
        #  запись ищется в значениях словаря
        for l_obj in self.dict_db.values():
            for obj in l_obj:
                if obj.pk == pk:
                    return obj
        return None

class Record:
    ''' fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - возраст человека (целое число).
    pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при создании каждого нового объекта;
    '''
    INDEX = 0

    def __init__(self, fio, descr, old):
        self.pk = Record.INDEX
        Record.INDEX += 1 
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self) -> int:
        '''вычисление хэша по атрибутам: fio и old (без учета регистра)'''
        return hash((self.old, self.fio.lower()))

    def __eq__(self, __o: object) -> bool:
        return self.old == __o.old and self.fio.lower() == __o.fio.lower()


s = '''Балакирев С.М.; программист; 33
Кузнецов А.В.; разведчик-нелегал; 35
Суворов А.В.; полководец; 42
Иванов И.И.; фигурант всех подобных списков; 26
Балакирев С.М.; преподаватель; 37
Балакирев С.М.; программист; 33'''
lst_in = [line for line in s.splitlines()]
#lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase()
for l in lst_in:
    s = l.split(';')
    db.write(Record(s[0], s[1], int(s[2])))
    
print(db.dict_db.values())
for i in range(0, Record.INDEX):
    o = db.read(i)
    print(o.fio, o.old)

bal = db.read(0)
print(db.dict_db[bal])

#tests

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"
    
if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"