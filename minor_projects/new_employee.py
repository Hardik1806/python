from abc import ABC ,abstractmethod 
def log_call(func):
    def wrapper(*args):
        print(f"[Log] calling {func.__name__}")
        return func(*args)
    return wrapper
def call(func):
    def wrapper(*args):
        print(f"[Log] calling {func.__name__} on {args[0].__class__.__name__}  class")
        return func(*args)
    return wrapper
class Employee():
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
    @abstractmethod
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
class WorkPolicy(ABC):
    @abstractmethod
    def policy():
        pass
    @abstractmethod
    def max_hours():
        pass


class Intern(Employee):
    def __init__(self,emp_name,salary):
        super().__init__(emp_name,salary)
    def work(self):
        print(f"{self.emp_name} is working as an Intern")
    @call
    def policy(self):
        print("Intern Works only 4 hours")
    @call
    def max_hours(self):
        print("4 is the maximum hours for Intern")
class PartTimeEmployee(Employee,WorkPolicy):
    @call
    def policy(self):
        print("PartTimeEmployee works for 6 hours")
    def max_hours(self):
        print("6 is the maximum hours for PartTimeEmployee")
obj_emp=[]
a=Employee("Hardik",-100)
b=Employee("Harish",10000)
c=Developer("Charlie",1000,"java")
obj_emp.append(a)
obj_emp.append(b)
obj_emp.append(c)
print(a.get_salary())
print(b.get_salary())
Employee.change_company("Google")
print(a.company_name)
Employee.get_headcount()
print(a.is_valid_salary(c.get_salary()))
c.work()
d=Tester("David",10000000)
e=Manager("Eve",100000000,4)
obj_emp.append(d)
obj_emp.append(e)
print("Day-2 after creating Tester and Manager")
d.work()
e.work()
print(f"After adding tester {Employee.total_employees} is the headcount")
x=e.can_approve(e.team_size)
print(x==False and "Manager cannot approve")
print("Manager can approve" if x==True else"") 
f=SeniorDeveloper("Frank",10000,"Python",5)
obj_emp.append(f)
f.work()
g=Intern("Grace",100000)
obj_emp.append(g)
print("Day-3 after adding Intern class which is a subclass of Employee and WorkPolicy ")
g.work()
g.policy()
print(f"{Employee.total_employees} is the headcount after adding intern class")
g.max_hours()
h=PartTimeEmployee("janice",6999)
h.policy()
h.max_hours()
emp_list=[]
n=len(obj_emp)
for i in range (n):
    x=obj_emp[i]
    z=x.emp_name
    emp_list.append(z)
print(name.upper()for name in emp_list)
