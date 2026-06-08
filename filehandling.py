class MyFile():
    def __init__(self,file_name):
        self.file_name=file_name
    def work(self):
        with open(self.file_name,"r") as f:
            content=f.read()
        print(content)
    def write(self):
        line=("hello python")
        with open(self.file_name,"w") as f1:
            f1.write(line)



file1=MyFile("todo.txt")
file1.write()
file1.work()
print(file1)

    

