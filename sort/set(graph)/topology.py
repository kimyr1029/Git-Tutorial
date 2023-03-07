#빌드트리, 선수강..
#진입차수 0을 큐에 추가
#큐를 꺼내 간선제거, 진입차수 0을 큐에 추가
from collections import deque

v,e =map(int,input().split())
indegree=[0]*(v+1)
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b) #a->b
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now=q.popleft()
        result.append(now) #q순서대로
        for i in graph[now]: #인접노드 진입차수 차감
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i, end=' ')
topology_sort()