#최소신장--사이클 없으면서 모두연결, 최단경로합(크루스칼)
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_set(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

edges=[]
result=0

for i in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges.sort() #비용순 정렬

for edge in edges:
    c,a,b=edge
    if find_parent(parent,a)==find_parent(parent,b):
        continue
    else:
        union_set(a,b) #연결
        result+=c #비용합산

print(result)
