def leng(g):
    count=0
    for i in g:
        count+=1
        if i==None:
             break
    
    return count



words=[]
n=int(input("enter the number of words"))
for i in range(n):
    a=input("enter the word")
    words.append(a)

length=[]
for i in range(n):
    b=leng(words[i])
    length.append(b)

print("lengths are:",length)
