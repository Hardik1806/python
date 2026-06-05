list_1=[]
n=int(input("please enter the number of elements u want in list "))
for i in range(n):
    a=int(input("please eneter the element"))
    list_1.append(a)

list_2=[]
list_3=[]
list1_len=len(list_1)
for i in range(int(list1_len/2)):
    list_2.append(list_1[i])

for i in range(int(list1_len/2),list1_len):
    list_3.append(list_1[i])

print(f"spllitted lists are: {list_2} , {list_3}")

