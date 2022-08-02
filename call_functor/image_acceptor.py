class ImageFileAcceptor:
    def __init__(self, acceptor):
        self.__acceptor = acceptor

    def __call__(self, *args, **kwds):
        s = args[0]
        return True if s.split('.')[-1] in self.__acceptor else False

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]