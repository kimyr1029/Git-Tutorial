#queue
from collections import deque

def bfs(graph,start,visited):
    q=deque()
    q.append(start)
    visited[start]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if visited[now]==False:
                q.append(now)
                visited[now]=True
    
    n=int(input())
    graph=[
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    visited=[False]*(n+1)
    bfs(graph,1,visited)