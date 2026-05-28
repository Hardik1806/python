list_1=[]
list_2=[]
n1=int(input("please enter the number of elements u want in the list"))
for i in range(n1):
    a=int(input("enter the element: "))
    list_1.append(a)

n2=int(input("please enter the number of elements u want in list 2"))
for i in range(n2):
    b=int(input("please eneter the element"))
    list_2.append(b)

#to combine to lists
list_combined=[]
for i in range(n1):
    list_combined.append(list_1[i])

for i in range(n2):
    list_combined.append(list_2[i])

print("combined list is: ",list_combined)


