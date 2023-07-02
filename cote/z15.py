n,m,k,x=map(int,input().split())
graph=[[1e9]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j]=0
                
#점화식 aij=aik +akj
for i in range(1,m+1):
    a,b=map(int,input().split())
    graph[a][b]=1 #a->b 1

for p in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][p]+graph[p][j])

result=[]
for i in range(1,n+1):
    if graph[x][i]==k:
        result.append(i)

result.sort()
if len(result)==0:
    print('-1')
else:
    for i in result:
        print(i,end=' ')
        