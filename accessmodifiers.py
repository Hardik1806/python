class accessmods:
    def __init__(self,name,_Class,__id):
        self.name=name
        self._Class=_Class
        self.__id=__id
    def privateaccess(self):
        print("private data can be accessed within  the same class",self.__id)

class subclass(accessmods):
    def protected(self):
        print("can be accessed via subclass",self._Class)

obj=accessmods("Hardik",12,1650)
print(obj.name)#it is public so it can be accessed always
print(obj._Class)# we can directly access protected data
obj.privateaccess()#method 1 of accessing private data
print(obj._accessmods__id)#method 2 of accessing private data
obj1=subclass("Hardik",12,1650)
obj1.protected()#method 2 of accessing protected data