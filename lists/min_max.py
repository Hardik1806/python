n=int(input("please enter the number of numbers u wanna eneter "))
num=[]
for i in range(n):
    a=int(input("enter tht numebr "))
    num.append(a)
print("maximum number is: ",max(num))
print("minimum number is: ",min(num))

