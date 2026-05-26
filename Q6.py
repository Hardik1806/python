import math
a=input("please enter the comma separated numbers: ")
new_list=[int(item) for item in a.split(",")]
print("the required list is: ",new_list)
count=0
for i in new_list:
    count+=1
for i in range(0,count-1):
    if(new_list[i]==new_list[i+1]):
        new_list.remove(new_list[i+1])

print("updated list without duplicates is: ",new_list)
new_list.sort()
print("sorted list is",new_list)
square=[math.pow(sqr,2) for sqr in new_list]
print("the squares are: ",square)
if not isinstance(a,str):
    raise TypeError("please enter a string")
if not isinstance(new_list,list):
    raise TypeError("it has to be a list")



