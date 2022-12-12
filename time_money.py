class Money:
    def __init__(self, tm = 0):
        self.__money = 0 
        self.set_money(tm)
        
    def set_money(self, tm):
        if self.__check_money(tm):
            self.__money = tm
        
    def get_money(self):
        return self.__money
    
    def add_money(self, tm):
        if type(tm) == Money:
            self.__money += tm.get_money()
    
    @classmethod
    def __check_money(cls, tm):
        return True if (type(tm) is int) and (0 <= tm) else False    

money = Money(4530)
print(money.get_money())
money1 = Money(200)
money.add_money(money1)
print(money.get_money())

