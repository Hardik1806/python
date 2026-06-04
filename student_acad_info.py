class InvalidMarks(Exception):
    pass
class School():
    pass
class Student(School):
    n=int(input("please enter the number of students"))
    def __init__(self,age,Class,address,subject,marks):
        self.age=age
        self.Class=Class
        self.address=address
        self.subject=subject
        self.marks=marks

    @classmethod
    def getInfo(cls):
        Age={}
        cLass={}
        Address={}
        Marks={}
        for i in range(0,cls.n):
            cls.age=int(input("please enter the age of student"))
            Age[i]=cls.age
            cls.Class=int(input("please enter the class of student "))
            cLass[i]=cls.Class
            cls.address=input(("please enter the address of the student"))
            Address[i]=cls.address
            cls.subject=input(("please enter the subject"))
            cls.marks=int(input("please enter the respective marks"))
            Marks[cls.subject]=cls.marks
        for i in range(0,cls.n):
            if Marks[cls.subject]<50:
                raise InvalidMarks("marks should be greater than 50")    
        count=1
        for i in range(0,cls.n):
            print(f"age of  student-{count} is : {Age[i]}")
            print(f"class of student-{count} is : {cLass[i]}")
            print(f"address of student-{count} is: {Address[i]}")
            count+=1
        print(f"marks in the respective subjects are: {Marks}")
        
Student.getInfo()




