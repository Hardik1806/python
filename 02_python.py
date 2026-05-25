class InvalidMulti(Exception):
    pass
def multiply(A,B):
    col_a=len(A[0])
    row_b=len(B)
    if col_a != row_b:
        raise InvalidMulti("not valid multiplication ")
    if not isinstance(A,list):
       raise TypeError("A has to be list")
    if not isinstance(B,list):
        raise TypeError("B has to be list")
    row_a=len(A)
    col_b=len(B[0])



    
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                B[i][j]=A[i][k]*B[k][j]
            
    for i in B:
        print(i)
           

A=[]
m=int(input("enter the number of rows in A;"))
n=int(input("enter the number of columns in A;"))
print("enter the elenebts of a")
for i in range(0,m):
    row=[]
    for j in range(0,n):
        num=int(input())
        try:
            if not isinstance(num,int):
                raise TypeError("integers allowed")
        except Exception as e:
            print("Error:",e)
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
        try:
            if not isinstance(num,int):
                raise TypeError("integer allowed")
        except Exception as e:
            print("Error:",e)
            row.append(num)
            B.append(row)      

multiply(A,B)
