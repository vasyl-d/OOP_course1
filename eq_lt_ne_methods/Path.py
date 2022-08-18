NUM = {int, float}

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        if type(to_x) in NUM and type(to_y) in NUM and type(max_speed) in NUM:
            self.to_x = to_x
            self.to_y = to_y
            self.max_speed = max_speed    
    
    def get_len(self, x, y):
        return ((self.to_x - x)**2 + (self.to_y - y)**2)**(1/2)

class Track:
    def __init__(self, start_x=0, start_y=0):
        if type(start_x) in NUM and type(start_y) in NUM:
            self.start_x = start_x
            self.start_y = start_y
        self.__track = []

    def add_track(self, tr:TrackLine):
        # - добавление линейного сегмента маршрута (следующей точки);
        if isinstance(tr, TrackLine):
            self.__track.append(tr)

    def get_tracks(self):
        # - получение кортежа из объектов класса TrackLine.
        return tuple(self.__track)
    
    def __str__(self):
        return f"{self.start_x}, {self.start_y}" + str([f"{i.to_x}, {i.to_y}" for i in self.get_tracks()])

    def __len__(self):
        '''Retrurn sum of len of track lines'''
        s = 0
        x = self.start_x
        y = self.start_y
        for i in self.__track:
            s += i.get_len(x, y)
            x = i.to_x
            y = i.to_y
        return int(s) 

    def __eq__(self, other:object) -> bool:
        if type(other) == Track:
            return len(self) == len(other)

    def __gt__(self, other:object) -> bool:
      if type(other) == Track:
            return len(self) > len(other)        

track1, track2 = Track(0,0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(track1)
print(track2)
print(res_eq)
print(len(track1))
print(len(track2))