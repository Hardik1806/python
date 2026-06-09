from datetime import date,datetime
def create_log(Date_Time,severity:list,work_list:list,message:list):
    length=len(work_list)
    with open("LogFile.txt","a") as f1:
        for i in range(length):
            result=f"{Date_Time}|{severity[i]}|Node worker-{work_list[i]} {message[i]}\n"
            f1.write(result)

d1=datetime.today().strftime("%Y-%m-%d %H:%M:%S")
workers_list=[]
n=int(input("please enter the number of workers u wanna have"))
for i in range(n):
    a=input("please enter the tag number")
    workers_list.append(a)
issue_severity=[]
for i in range(n):
    b=input("enter the severity of the issue like:Critical/High/Medium/Low")
    issue_severity.append(b)
random_message=[]
for i in range(n):
    c=input("enter the message u wanna print")
    random_message.append(c)
create_log(d1,issue_severity,workers_list,random_message)

