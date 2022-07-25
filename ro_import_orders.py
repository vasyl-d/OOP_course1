import time
import json
import requests
import math


API_KEY = "237a1231fe9b4a13b66e5389598b9d85"
RO_PATH = "https://api.remonline.app"

class DictObj:
    '''класс для преобразования json в обьект'''
    def __init__(self, in_dict:dict):
       	if isinstance(in_dict, dict):
            for key, val in in_dict.items():
                if isinstance(val, (list, tuple)):
                    setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
                else:
                    setattr(self, key, DictObj(val) if isinstance(val, dict) else val)
        else:
            assert False, 'must be dict in parm'


class RemOnline():
    __instance_id = None
    token = None
    token_lifetime = None
    def __new__(cls):
        if cls.__instance_id == None:
             cls.__instance_id = super().__new__(cls)
        return cls.__instance_id 

    def __init__(self) -> None:
        self.tokenize()

    def tokenize(self):
        if self.token == None or self.is_token_invalid():
            self.token = self.set_token()
            self.token_lifetime = time.time()+550
        return False if self.token == None else True

    def is_token_invalid(self):
        return True if self.token_lifetime <= time.time() else False

    def set_token(self):
        url = RO_PATH+'/token/new'
        token = None
        payload={'api_key': API_KEY}
        files=[

        ]
        headers = {}
        try:
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            response.raise_for_status()
            data = json.loads(response.text)
            token = data["token"]
        except Exception as error:
            print(error)
        
        return token


class GetResurs:
    '''класс для итерации по Гет запросам, пагинация по 50 єлементов'''
    
    def __init__(self, ro:RemOnline, resurs:str, filterstr:str=''):
        self.ro = ro
        self.resurs = resurs
        self.res = None
        self.filterstr = filterstr
        self.page_len = 50

    def __iter__(self):
        self.limit = 1
        self.page = 1
        return self

    def __next__(self):
        if self.page <= self.limit:
            headers = {}
            payload = {}
            files ={}
            if not self.ro.tokenize():
                return self.res 
                
            url = RO_PATH + self.resurs + '?token='+str(self.ro.token)
            if self.filterstr !='':
                url +='&'+ self.filterstr
            if self.page >1 :
                url += '&page='+str(self.page)
            try:
                print(url)
                response = requests.request("GET", url, data=payload, headers=headers, files=files)
                response.raise_for_status()
                data = json.loads(response.text)
                self.limit = math.ceil(int(data["count"])/self.page_len)
                self.res = DictObj(response.json()) #- так можно вернуть страницу как объект
            except Exception as error:
                print(error)
            self.page += 1
            return self.res
        else:
            raise StopIteration                    

class Warehouse():
    id = None # integer
    is_global = None #bool - Чи є склад глобальным?
    title = None # string - Назва склад
    branch_id = None #Branch

class Branch():
    id = None
    title = None

ro = RemOnline()
print(ro.token, ro.token_lifetime)

re = GetResurs(ro, '/lead/') #запрос списка лидов
myiter = iter(re)
'''каждая страница - объект. его свойство data содержит массив объектов с содержимым строки.'''
for i in myiter:
    for j in i.data:
        print(j.contact_name)
            
wh = GetResurs(ro, '/warehouse/goods/67724') #получим список товаров
myiter = iter(wh)
for i in myiter:
    for j in i.data:
        print(j.title)

wh = GetResurs(ro, '/warehouse/') #получим список складов
myiter = iter(wh)
for i in myiter:
    for j in i.data:
        print(j.id, j.title)

wh = GetResurs(ro, '/clients/') #получим список клиентов
myiter = iter(wh)
#возьмем только 1 cраницу
page = next(myiter)
for client in page.data:
    print(client.name, client.id)


tm = time.struct_time((2022,7,18,0,0,0,0,0,0))
tday1 = round(time.mktime(tm))*1000
tday2 = round(time.time())*1000

flt = "created_at[]="+str(tday1)+"&created_at[]="+str(tday2)
print(flt)
ord = GetResurs(ro, '/order/', flt)
myiter = iter(ord)
#возьмем только 1 cраницу
page = next(myiter)
for order in page.data:
    print(order.id, order.id_label, order.client.name, order.status.name, order.created_at)