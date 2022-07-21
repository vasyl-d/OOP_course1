class Video:
    def __init__(self):
        self.name = ''

    def create(self, name): # для задания имени name текущего видео (метод сохраняет имя name в локальном атрибуте name объекта класса Video);
        self.name = name
        
    def play(self): #  для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").
        print (f'воспроизведение видео {self.name}')
    
class YouTube:
    videos = []
    
    @classmethod
    def add_video(cls, video): # для добавления нового видео (метод помещает объект video класса Video в список);
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx): # для проигрывания видео из списка по указанному индексу (индексация с нуля).
        cls.videos[video_indx].play()

v1 = Video()
v2 = Video()
v1.create('Python')
v2.create('Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)

