class FileAcceptor:
    def __init__(self, *args):
        self.acc_names = set(args) if args else set()

    def __call__(self, filename):
        ext = filename.split('.')[-1]
        return True if ext in self.acc_names else False

    def __add__(self, __o: object):
        return FileAcceptor(*self.acc_names.union(__o.acc_names)) if type(__o) is FileAcceptor else self

    def __radd__(self, __o: object):
        return self.__sum__(__o)

    def __str__(self):
        return " ".join(self.acc_names)


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls", "noext.", "noextnocomma", "some.bmp"]
acceptor = FileAcceptor('jpg', 'png', 'jpeg')
print(acceptor)
acc2 = FileAcceptor('jpg', 'bmp','tiff')
acc3 = acceptor + acc2
print(acc3)
filenames = list(filter(acc3, filenames))
print(filenames)