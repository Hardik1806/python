def log_call(func):
   def wrapper(*args):
        print(f"[Log] calling {func.__name__}")
        return func(*args)
   return wrapper
class HandleFile():
   def __init__(self,file_name):
      self.file_name=file_name   
   @log_call
   def write(self):
      content_write=input("please enter the content u wanna write")
      with open(self.file_name,"w") as f:
         f.write(content_write)
   def read(self):
      with open(self.file_name,"r") as f:
         a=f.read()
         b=f.readlines()
      return a,b
   def append(self):
       data_append=input("please enter what alert u wanna append")
       with open(self.file_name,"a") as f:
          f.write(data_append)
   def search_file(self,keyword="severity"):
       info_line=[]
       with open(self.file_name,"r")as f:
           for line in f:
               if keyword in line:
                   info_line.append(line)
                   print(line)
   def count_searches(self):
       no_of_warn=0
       n=len(self.info_line)
       for i in range(n):
           if "critical" in self.info_line[i]:
               no_of_warn+=1
       return no_of_warn