def decorator(func):
    func()
class Employee:
    count=0
    def __init__(self,company_name,emp_name,salary,):
        self.company_name=company_name
        self.emp_name=emp_name
        self.__salary=salary
        Employee.count+=1
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,x):
        try:
            if(x<0):
                raise ValueError("salary cannot be negative")
            self.__salary=x
        except ValueError as e:
            print("Error:",e)
    def work(self):
        print(f"{self.emp_name} is working")
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
    @staticmethod
    def is_valid_salary(salary):
        if(salary>0):
            return True
        
    @classmethod
    def get_headcount(cls):
        print("number of employees is: ",cls.count)

class Developer(Employee):
    def __init__(self,company_name,emp_name,salary,lang):
        super().__init__(company_name,emp_name,salary)
        self.lang=lang
    def work(self):
        print(f"{self.emp_name} is coding in {self.lang}")

a=Employee("IBM","Hardik",100)
b=Employee("Google","Harish",10000)
c=Developer("TCS","nilesh",1000,"python")
print(a.company_name)
print(a.emp_name)
print(b.emp_name)
a.work()
b.work()
Employee.get_headcount()
a.change_company("Dell")
print(a.company_name)

