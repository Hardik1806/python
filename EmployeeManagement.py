from abc import ABC,abstractmethod
def decorator(func):
    func()
class Employee:
    def __init__(self,company_name,name,__salary):
        self.company_name=company_name
        self.name=name
        self.__salary=__salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,x):
        try:
            self.__salary=x
            if(x<0):
                raise ValueError("salary should be positive")
        except ValueError as e:
            print("Error:",e)
    @abstractmethod
    def work(self):
        print(f"{self.name} is working.")
    @classmethod
    def change_company(cls,new_name):
        cls.new_name=new_name
    @staticmethod
    def is_valid_salary(__salary):
        if __salary>0:
            return True
    count=0
    @classmethod
    def get_headcount():
        count+=1
        print("the head count is :",count)

    
class Developer(Employee):
    def __init__(self,company_name,name,__salary,prog_lang):
        super().__init__(company_name,name,__salary)
        self.prog_lang=prog_lang
    
    def work(self):
        print(f"{self.name} is coding in language {self.prog_lang}")


class Tester(Employee):
    def word(self):
        print(f"{self.name} is testing software")

class Manager(Employee):
    def __init__(self,company_name,name,__salary,prog_lang,team_size):
        super().__init__(company_name,name,__salary,prog_lang)
        self.team_size=team_size
    def word(self):
        print(f"{self.name} is managing a team of {self.team_size}")
    
    @staticmethod
    def can_approve(team_size):
        if team_size>=5:
            return True
class SeniorDeveloper(Developer):
    def __init__(self,company_name,name,__salary,prog_lang,team_size,years_experience):
        super().__init__(company_name,name,__salary,prog_lang,team_size)
        self.years_experience=years_experience
    def work(self):
        print(f"{self.name} is leading development in {self.prog_lang} with {self.years_experience} years exp")
class WorkPolicy():
    @abstractmethod
    def policy():
        pass
class Intern(Employee,WorkPolicy):
    def policy(self):
        print("Interns only works 4 hours")
    def work(self):
        print(f"{self.name} is learning as an intern")

    
class TechLead(Developer,Manager):
    def __init__(self,company_name,name,__salary,prog_lang,team_size,project_name):
        super().__init__(company_name,name,__salary,prog_lang,team_size)
        self.project_name=project_name
        @decorator
        def work():
            print("LOG calling")
        work()
print("Mro of Intern class is: ",Intern.mro())
print("Mro of techlead class is: ",TechLead.mro())