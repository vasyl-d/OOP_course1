# здесь объявляйте класс PrimaryKey
class PrimaryKey:
    def __enter__(self):
        print("вход")
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(exc_type)
        return True


with PrimaryKey() as pk:
    raise ValueError