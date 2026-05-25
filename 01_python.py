def multiply(A,B):
    row_a=len(A)
    col_a=len(A[0])
    row_b=len(B)
    col_b=len(B[0])
    if col_a!= row_b:
        print("not valid multiplication ")
    
    c= [[0 for _ in range(col_b)] for _ in range(row_a)]
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                c[i][j]+=A[i][k]*B[k][j]
            
    for i in c:
        print(i)
           

A=[]
m=int(input("enter the number of rows in A;"))
n=int(input("enter the number of columns in A;"))
print("enter the elenebts of a")
for i in range(0,m):
    row=[]
    for j in range(0,n):
        num=int(input())
        row.append(num)
    A.append(row)


B=[]
p=int(input("enter the number of rows in B;"))
q=int(input("enter the number of columns in B;"))
print("enter the elenebts of b")
for i in range(0,p):
    row=[]
    for j in range(0,q):
        num=int(input())
        row.append(num)
    B.append(row)      

multiply(A,B)

