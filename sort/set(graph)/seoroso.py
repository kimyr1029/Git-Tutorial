#union - find
#서로 다른 집합 나누기, 팀가르기
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
cycle=False
for i in range(1,n+1):
    parent[i]=i #자기자신 초기화
for i in range(m):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b): #같은 부모/루트 존재 cycle
        cycle=True
        break
    else:
        union_set(parent,a,b)
if cycle:
    print('cycle')
for i in range(1,n+1):
    print(find_parent(parent,i),end=' ')
print()
for i in range(1,n+1):
    print(parent[i],end=' ')