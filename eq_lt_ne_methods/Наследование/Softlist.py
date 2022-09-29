class SoftList(list):
    def __getitem__(self, key):
        try:
            res = super().__getitem__(key)
        except:
            res = False
        return res

sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
print(sl[-7]) # False