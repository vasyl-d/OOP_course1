class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024

Goods.price = 2048
Goods.inflation = 100

#создать пустой класс, добавить ему атрибуті и вівести знячене
class Car:
    pass
   
setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__["color"])

class Dictionary:
    rus = "Питон"
    eng = "Python"

print(getattr(Dictionary, 'rus_word', False))

car1 = Car()
car1.ddd = '222'
car1.sss = 'asdf'
car1.hhh = 'fff'

delattr(car1, 'ddd')
print(*car1.__dict__)
print(hasattr(car1, 'hhh'))

class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

    def set_coords(self, x , y):
        self.x = x
        self.y = y

p1 = Person()
print(hasattr(p1,'job')) #наличие атрибута у класса
print(True if p1.__dict__.get('job') else False) #наличие атрибута у єкземпляра
p1.set_coords(12, 23)
print(p1.x, p1.y)

class MediaPlayer:
    def open(self,file):
        self.filename = file
    
    def play(self):
        print("Воспроизведение ", self.filename)
        
        
media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media2.play()

class Graph:
    LIMIT_Y = [0, 10]
        
    def set_data(self, data): 
        self.data = data

    def draw(self):
        [print(x, end=" ",) for x in self.data if (x >= self.LIMIT_Y[0] and x <=self.LIMIT_Y[1])]
        
graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()