class Graph:
    def __init__(self, data=[], is_show=True):
        self.data = data[:]   #копируем исходные данные (создаем отдельный)
        self.is_show = is_show

    def pr_show(self):
        if self.is_show == False:
            print("Отображение данных закрыто") 
            return False
        return True

    def set_data(self, data): # для передачи нового списка данных в текущий график;
        self.data = data

    def show_table(self): # для отображения данных в виде строки из списка чисел (числа следуют через пробел);
        if self.pr_show(): 
            print(*self.data)

    def show_graph(self): # для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
        if self.pr_show():
            print("Графическое отображение данных:", *self.data)

    def show_bar(self): # для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
        if self.pr_show():
            print("Столбчатая диаграмма:",*self.data)

    def set_show(self, fl_show): # метод для изменения локального свойства is_show на переданное значение fl_show.
        self.is_show = fl_show

data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()

