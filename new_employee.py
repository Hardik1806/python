def log_call(func):
    def wrapper(*args,**kwargs):
        print(f"[Log] calling {func.__name__}")
        return func(*args,**kwargs)
    return wrapper
class Employee:
    total_employees=0
    company_name="IBM"
    def __init__(self,emp_name,salary,):
        self.emp_name=emp_name
        self.__salary=0
        self.set_salary(salary)
        Employee.total_employees+=1
    @log_call
    def get_salary(self):
        return self.__salary
    def set_salary(self,x):
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
        else:
            return False
        
    @classmethod
    def get_headcount(cls):
        print("number of employees is: ",cls.total_employees)

class Developer(Employee):
    def __init__(self,emp_name,salary,lang):
        super().__init__(emp_name,salary)
        self.lang=lang
    def work(self):
        print(f"{self.emp_name} is coding in {self.lang}")
class Tester(Employee):
    def __init__(self,emp_name,salary):
        super().__init__(emp_name,salary)
    def work(self):
        print(f"{self.emp_name} is testing software")
class Manager(Employee):
    def __init__(self,emp_name,salary,team_size):
        super().__init__(emp_name,salary)
        self.team_size=team_size
    def work(self):
        print(f"{self.emp_name} is managing a team of {self.team_size} employees")
    @staticmethod
    def can_approve(team_size):
        if(team_size>=5):
            return True
        else:
            return False
class SeniorDeveloper(Developer):
    def __init__(self,emp_name,salary,lang,years_experience):
        super().__init__(emp_name,salary,lang)
        self.years_experience=years_experience
    def work(self):
        print(f"{self.emp_name} is leading development in {self.lang} with {self.years_experience} years exp")

a=Employee("Hardik",-100)
b=Employee("Harish",10000)
c=Developer("nilesh",1000,"python")
d=Tester("Raman",10000000)
e=Manager("Kartik",100000000,10)
print(b.get_salary())
print(b.company_name)
print(a.change_company("Dell"))
print(b.company_name)
c.work()
d.work()
e.work()
print(Employee.get_headcount())
print(Employee.is_valid_salary(-100))
f=SeniorDeveloper("Rishabh",10000,"java",8)
f.work()

