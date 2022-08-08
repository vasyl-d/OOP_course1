class ValidateTm:

    def __init__(self) -> None:
        pass
    def validate(self, value):
        return True if type(value) == int and 0 <= value else False

class Tm:
    #descriptor
    def __init__(self, validator:ValidateTm=ValidateTm()) -> None:
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name) 
 
    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)
        else:
            raise ValueError("Должно быль целое положительное")

class Clock:
    hours = Tm()
    minutes = Tm()
    seconds = Tm()

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:05}"

    def get_time(self): 
        # возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, cl1:Clock, cl2:Clock):
        self.cl1 = cl1
        self.cl2 = cl2

    def __call__(self):
        # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
        l = self.get_dt()
        s = self.dt_str(l)
        return s

    def __len__(self):
        # разницу времен clock1 - clock2 в секундах (целое число)
        return self.get_dt()

    def __str__(self):
        # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
        l = self.get_dt()
        s = self.dt_str(l)
        return s

    def get_dt(self):
        l = self.cl1.get_time()-self.cl2.get_time()
        return l if l > 0 else 0
  
    def dt_str(self, l):
        h = l//3600
        m = (l - h*3600)//60
        s = l - h*3600 - m*60
        return f"{h:02}: {m:02}: {s:02}"

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt) 