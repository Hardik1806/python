import os
class MyFile():
    def __init__(self,file_name):
        self.file_name=file_name
    def read(self):
        text=input("please enter text u wanna append")
        with open(self.file_name,"w") as f:
            f.write("Day-1\n")
        with open(self.file_name,"a") as f1:
            f1.write(text)
        if not self.exists():
            print(f"{self.file_name} does not exists")
            return " "
        
    def give(self):
        with open(self.file_name,"r") as f:
            a=f.read()
            print(a)   
    def exists(self):
        return os.path.exists(self.file_name)
            
    def read_lines(self):
        with open(self.file_name,"r") as f:
            lines=f.readlines()
            return lines
    def count_lines(self):
        a=len(self.read_lines)
        return a

file1=MyFile("run.txt")
file1.read()
file1.give()
file1.exists()
file1.read_lines()
file1.count_lines()

    

