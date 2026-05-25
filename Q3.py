li=[]
a=int(input("please enter the number of names u wanna enter"))
for i in range(a):
    b=input("please enter the name")
    li.append(b)
l2=[]
for i in range(a):
    h=li[i].upper()
    l2.append(h)

print("uppercase list : ",l2)
