class DateError(Exception):
    def __str__(self) -> str:
        return 'Неверный формат даты'

class DateString:
    def __init__(self, date_string):
            self.day, self.month, self.year = self.is_correct(date_string)
    
    @staticmethod
    def is_correct(str):
        try:
            day, month, year = tuple(map(int, str.split('.')))
        except Exception as e:
            raise DateError()
        else:
            if not(1 <= day <= 31 and 1 <= month <= 12 and 0 <=year <= 3000):
                raise DateError()
        return (day, month, year)


    def __str__(self) -> str:
        return f"{self.day :02d}.{self.month :02d}.{self.year :04d}"


# 
date_string = input()

try:
    d1 = DateString(date_string)
    print(d1)
except DateError as e:
    print(e)