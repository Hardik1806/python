student={}
marks={}
n=int(input("please enter the number of students:"))
for i in range(0,n):
    name=input("enter name of student")
    subject=input("enter the subject")
    mark=int(input("ente the marks"))
    student[i]=name
    marks[subject]=mark

if "maths" not in marks:
    raise ValueError("required subject not found")
if not isinstance(name,str):
    raise TypeError("please enter valid input")
print("detaikls entered are")
for i in range(0,n):
    print(f"name of student is {student[i]}")
print(f"subject with respective marks is {marks}")
sum=0
count=0
for maths in marks:
    sum+=marks["maths"]
    count+=1

average=sum/count

print("avergae maths markse are: ",average)



