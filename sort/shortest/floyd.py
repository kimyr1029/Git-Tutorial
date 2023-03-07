# #모든경로 최단거리, 인접행렬
# #DP Dab=min(Dab,Dac+Dcb)
# #자기자신은 0
# v,e=map(int,input().split())
# INF=int(1e9)
# graph=[[INF]*(v+1) for _ in range(v+1)]

# for i in range(v+1):
#     for j in range(v+1):
#         if i==j:
#             graph[i][j]=0 #자기자신 초기화
# for i in range(e):
#     a,b,c=map(int,input().split())
#     graph[a][b]=c

# #점화식
# for k in range(1,v+1):
#     for i in range(1,v+1):
#         for j in range(1,v+1):
#             graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# for i in range(1,v+1):
#     for j in range(1,v+1):
#         if graph[i][j]==INF:
#             print('INF',end=' ')
#         else:
#             print(graph[i][j],end=' ')
#     print()
import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
distance=[INF]*(v+1)

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0 #첫 시작
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist: #최단값상태
            continue
        for i in graph[now]: #인접노드
            node,cost=i[0],i[1]
            cost=cost+dist #거리갱신
            if cost<distance[node]: #인접노드까지 거리 갱신
                distance[node]=cost
                heapq.heappush(q,(cost,node)) #큐삽입
dijkstra(start)

for i in range(v+1):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])