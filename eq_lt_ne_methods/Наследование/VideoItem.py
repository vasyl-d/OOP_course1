class VideoRating:
    def __init__(self, rating=0):
        self.rating = rating

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, value):
        if value in {0,1,2,3,4,5}:
            self.__rating = value
        else:
            raise ValueError('неверное присваиваемое значение')

class VideoItem:
    rating: VideoRating
    def __init__(self,title:str, descr:str, path:str):
        self.title, self.descr, self.path, self.rating = title, descr, path, VideoRating()

    
v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
try:
    v.rating.rating = 6
except ValueError:
    assert True
else:
    assert False, "Rating must be in [0,5] range" 


