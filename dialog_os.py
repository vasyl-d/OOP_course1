TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    name = ''
    def __new__(cls, *args, **kwargs):
        cls.name = args[0]
        if TYPE_OS == 2:
            dg = DialogLinux()
        elif TYPE_OS == 1:
            dg = DialogWindows()
        dg.name = cls.name
        return dg


dlg = Dialog('yjvth 1 windows')
TYPE_OS = 2 
dlg2 = Dialog('2 linux')

print( dlg.name_class, dlg2.name_class)

