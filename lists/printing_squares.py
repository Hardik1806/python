import math
numbers=[]
n=int(input("please enter numbers from 1 to 10: "))
for i in range(n):
    a=int(input("enter the number"))
    numbers.append(a)
print("the numbers entered are: ")
for i in range(n):
    print(numbers[i]," ")

square=[sqr for sqr in numbers if((math.sqrt(sqr)).is_integer())]
print("the squares are: ", square)



