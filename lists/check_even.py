a=int(input("please enter the number of numbers u want to check: "))
l1=[]
for i in range(a):
    b=int(input("enter the number:"))
    l1.append(b)
print("the numbers entered are: ",l1)
check=[ch for ch in l1 if(ch%2==0)]
print("the even numbers are: ",check)


