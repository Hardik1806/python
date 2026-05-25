a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[1,2,3],
   [4,5,6],
   [7,8,9]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]]
rows=len(a)
cols=len(a[0])
for i in range(rows):
    for j in range(cols):
        for k in range (cols):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]

for i in c:
    print(i)
    
