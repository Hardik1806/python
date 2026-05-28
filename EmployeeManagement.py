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
        self.__salary=x

    def work(self):
        print(f"{self.name} is working.")
    
class Developer(Employee):
    def __init__(self,company_name,name,__salary,prog_lang):
        super().__init__(company_name)
        super().__init__(name)
        super().__init__(__salary)
        self.prog_lang=prog_lang
    
    def work(self):
        print(f"{self.name}. is coding in language {self.prog_lang}")


class Tester(Employee):
     pass



