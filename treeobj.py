class TreeObj:
    def __init__(self, indx, value=None): 
        self.__left = None #- ссылка на следующий объект дерева по левой ветви (изначально None);
        self.__right = None #- ссылка на следующий объект дерева по правой ветви (изначально None).
        self.indx = indx #int
        self.value = value #str
    @staticmethod
    def is_norm(obj):
        return True if type(obj) in (TreeObj, None) else False

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, left):
        if self.is_norm(left):
            self.__left = left

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, right):
        if self.is_norm(right):
            self.__right = right

        

class DecisionTree:
    @classmethod
    def predict(cls, root:TreeObj, x):
        ''' для построения прогноза (прохода по решающему дереву)
        для вектора x из корневого узла дерева root'''
        next = root.left if x[root.indx]  else root.right 
        if next == None:
            return root.value
        else:
            return cls.predict(next, x)

    @classmethod
    def add_obj(cls, obj:TreeObj, node=None, left=True) -> TreeObj:
        '''для добавления вершин в решающее дерево 
        (метод должен возвращать добавленную вершину - объект класса TreeObj)
        node - ссылка на вершину к которой цепляемся (т.е. у корня = None), 
        left - Тру е если цепояемся к левой ветке, Фалс - если к правой'''
        if node != None:
            if left:
                if node.left == None:
                    node.left = obj
            else:
                if node.right == None:
                    node.right = obj
        return obj

root = DecisionTree.add_obj(TreeObj(0, "Любит питон"))
v_11 = DecisionTree.add_obj(TreeObj(1, "Понимает ООП"), root)
v_12 = DecisionTree.add_obj(TreeObj(2, "Любит кунг-фу панда"), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)