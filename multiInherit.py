class School:
    def __init__(self,classes,affiliationtype):
        self.classes=classes
        self.affiliationtype=affiliationtype
    
class Classes:
    def __init__(self,classTeacher,HOD):
        self.classTeacher=classTeacher
        self.HOD=HOD
class Students(Classes,School):
    def __init__(self,n,name,age,classes,affiliationtype,classTeacher,HOD):
        School.__init__(self,classes,affiliationtype)
        Classes.__init__(self,classTeacher,HOD)
        self.n=n
        self.name=name
        self.age=age

obj1=Students(5,"hardik",18,12,"CBSE","XYZ","LMNO")
a=obj1.name
b=obj1.classTeacher
c=obj1.affiliationtype
print(a)
print(b)
print(c)